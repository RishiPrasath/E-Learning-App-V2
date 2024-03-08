from typing import TYPE_CHECKING, Any, Callable, ClassVar, Dict, Generic, Optional, Type, TypeVar, List

if TYPE_CHECKING:
    ...

from reloadium.vendored.envium import EnvGroup, Environ, env_var

__RELOADIUM__ = True

__all__ = ["PubEnv", "env"]


class Ide(EnvGroup):
    type: Optional[str] = env_var(default=None)
    name: Optional[str] = env_var(default=None)
    version: Optional[str] = env_var(default=None)
    plugin_version: Optional[str] = env_var(default=None)
    server_port: Optional[int] = env_var(default=None)


class Profiling(EnvGroup):
    enabled: bool = env_var(default=True)
    partials: bool = env_var(default=True)


class FastDebug(EnvGroup):
    whole_project: Optional[bool] = env_var(default=False)


class PubEnv(Environ):
    events_grace_period: float = env_var(default=0.7)
    merge_events_period: float = env_var(default=0.2)
    page_reload_on_start: bool = env_var(default=True)
    verbose: bool = env_var(default=True)
    docker: bool = env_var(default=False)
    remote: bool = env_var(default=False)
    reloadiumpath: str = env_var(raw=True, default="")
    reloadiumignore: str = env_var(raw=True, default="")
    cache: bool = env_var(True)
    print_logo: bool = env_var(default=True)
    watch_cwd: bool = env_var(default=True)
    user_id: Optional[str] = env_var()
    parent_run_id: Optional[str] = env_var()
    sub_process: int = env_var(default=0)
    quick_config: Optional[str] = env_var()
    debug: Optional[bool] = env_var()
    extra_watched_files: str = env_var(default="")
    watch_files_with_breakpoints: bool = env_var(default=True)
    license_key: Optional[str] = env_var()
    active_files: str = env_var(default="")

    ide = Ide()
    fast_debug = FastDebug()
    profiling = Profiling()


env = PubEnv(name="rw", load=True)
