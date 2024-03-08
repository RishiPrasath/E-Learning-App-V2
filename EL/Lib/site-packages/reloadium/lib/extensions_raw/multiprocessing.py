import sys

__RELOADIUM__ = True


def posix_popen_launch(self2, process_obj):
    from reloadium.lib.environ import env
    from pathlib import Path
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    import io
    import os

    env.sub_process += 1
    env.save_to_os_environ()

    def close_fds(*fds):
        """Close each file descriptor given as an argument"""
        for fd in fds:
            os.close(fd)

    if sys.version_info > (3, 8):
        from multiprocessing import resource_tracker as tracker
    else:
        from multiprocessing import semaphore_tracker as tracker

    tracker_fd = tracker.getfd()
    self2._fds.append(tracker_fd)
    prep_data = spawn.get_preparation_data(process_obj._name)
    fp = io.BytesIO()
    set_spawning_popen(self2)

    try:
        reduction.dump(prep_data, fp)
        reduction.dump(process_obj, fp)
    finally:
        set_spawning_popen(None)

    parent_r = child_w = child_r = parent_w = None
    try:
        parent_r, child_w = os.pipe()
        child_r, parent_w = os.pipe()
        cmd = spawn.get_command_line(tracker_fd=tracker_fd,
                                     pipe_handle=child_r)

        file = str(Path(prep_data["sys_argv"][0]).absolute())
        cmd = [cmd[0], "-B", "-m", "reloadium_launcher", "spawn_process", str(tracker_fd),
               str(child_r), file]
        self2._fds.extend([child_r, child_w])
        self2.pid = util.spawnv_passfds(spawn.get_executable(),
                                       cmd, self2._fds)
        self2.sentinel = parent_r
        with open(parent_w, 'wb', closefd=False) as f:
            f.write(fp.getbuffer())
    finally:
        fds_to_close = []
        for fd in (parent_r, parent_w):
            if fd is not None:
                fds_to_close.append(fd)
        self2.finalizer = util.Finalize(self2, close_fds, fds_to_close)

        for fd in (child_r, child_w):
            if fd is not None:
                os.close(fd)


def wind32_popen_launch(self2, process_obj):
    from reloadium.lib.environ import env
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    from multiprocessing.popen_spawn_win32 import TERMINATE, WINEXE, WINSERVICE, WINENV, _path_eq
    from pathlib import Path
    import os
    import msvcrt
    import sys
    import _winapi

    env.sub_process += 1
    env.save_to_os_environ()

    if sys.version_info > (3, 8):
        from multiprocessing import resource_tracker as tracker
        from multiprocessing.popen_spawn_win32 import _close_handles
    else:
        from multiprocessing import semaphore_tracker as tracker
        _close_handles = _winapi.CloseHandle

    prep_data = spawn.get_preparation_data(process_obj._name)

    # read end of pipe will be duplicated by the child process
    # -- see spawn_main() in spawn.py.
    #
    # bpo-33929: Previously, the read end of pipe was "stolen" by the child
    # process, but it leaked a handle if the child process had been
    # terminated before it could steal the handle from the parent process.
    rhandle, whandle = _winapi.CreatePipe(None, 0)
    wfd = msvcrt.open_osfhandle(whandle, 0)
    python_exe = spawn.get_executable()
    file = str(Path(prep_data["sys_argv"][0]).absolute())
    cmd = " ".join([python_exe, "-B", "-m", "reloadium_launcher", "spawn_process",
           str(os.getpid()), str(rhandle), file])

    # bpo-35797: When running in a venv, we bypass the redirect
    # executor and launch our base Python.
    if WINENV and _path_eq(python_exe, sys.executable):
        python_exe = sys._base_executable
        env = os.environ.copy()
        env["__PYVENV_LAUNCHER__"] = sys.executable
    else:
        env = None

    with open(wfd, 'wb', closefd=True) as to_child:
        # start process
        try:
            hp, ht, pid, tid = _winapi.CreateProcess(
                python_exe, cmd,
                None, None, False, 0, env, None, None)
            _winapi.CloseHandle(ht)
        except:
            _winapi.CloseHandle(rhandle)
            raise

        # set attributes of self
        self2.pid = pid
        self2.returncode = None
        self2._handle = hp
        self2.sentinel = int(hp)
        if sys.version_info > (3, 8):
            self2.finalizer = util.Finalize(self2, _close_handles,
                                           (self2.sentinel, int(rhandle)))
        else:
            self2.finalizer = util.Finalize(self2, _close_handles,
                                            (self2.sentinel,))

        # send information to child
        set_spawning_popen(self2)
        try:
            reduction.dump(prep_data, to_child)
            reduction.dump(process_obj, to_child)
        finally:
            set_spawning_popen(None)
