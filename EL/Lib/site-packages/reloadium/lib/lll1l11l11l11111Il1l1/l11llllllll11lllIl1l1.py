from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type, cast
import types

from reloadium.corium.llll1ll111111lllIl1l1 import llll1ll111111lllIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1.l1111ll1l1l11111Il1l1 import lll1lllll11ll11lIl1l1
from reloadium.lib.environ import env
from reloadium.corium.ll111ll1ll11ll1lIl1l1 import ll11l11lll1ll111Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll1l1ll11lll11l1Il1l1 import lllll111l1l1l1llIl1l1
from reloadium.corium.l11111l1ll1ll111Il1l1 import ll111l1ll11lllllIl1l1, lll1ll1ll111llllIl1l1, lll11l1ll11l1ll1Il1l1, l111l111l111ll11Il1l1
from reloadium.corium.lll11ll1ll1111l1Il1l1 import l111ll1l1l11l11lIl1l1
from dataclasses import dataclass, field

__RELOADIUM__ = True

l1ll11l111l11ll1Il1l1 = llll1ll111111lllIl1l1.l11ll1l1ll111111Il1l1(__name__)


@dataclass(**l111l111l111ll11Il1l1)
class lll1l11l11ll11llIl1l1(lll11l1ll11l1ll1Il1l1):
    ll1l11lll1111l11Il1l1 = 'FlaskApp'

    @classmethod
    def l11l1lllll111111Il1l1(l1lll1111111ll11Il1l1, ll1lll11lll11lllIl1l1: l111ll1l1l11l11lIl1l1.l111ll111llll111Il1l1, lll1l11lll1lllllIl1l1: Any, llll1ll1l111lll1Il1l1: ll111l1ll11lllllIl1l1) -> bool:
        import flask

        if (isinstance(lll1l11lll1lllllIl1l1, flask.Flask)):
            return True

        return False

    def lll1lll111l11lllIl1l1(ll111ll111ll1lllIl1l1) -> bool:
        return True

    @classmethod
    def l1lll1l1l1l11lllIl1l1(l1lll1111111ll11Il1l1) -> int:
        return (super().l1lll1l1l1l11lllIl1l1() + 10)


@dataclass(**l111l111l111ll11Il1l1)
class l111111llllll11lIl1l1(lll11l1ll11l1ll1Il1l1):
    ll1l11lll1111l11Il1l1 = 'Request'

    @classmethod
    def l11l1lllll111111Il1l1(l1lll1111111ll11Il1l1, ll1lll11lll11lllIl1l1: l111ll1l1l11l11lIl1l1.l111ll111llll111Il1l1, lll1l11lll1lllllIl1l1: Any, llll1ll1l111lll1Il1l1: ll111l1ll11lllllIl1l1) -> bool:
        if (repr(lll1l11lll1lllllIl1l1) == '<LocalProxy unbound>'):
            return True

        return False

    def lll1lll111l11lllIl1l1(ll111ll111ll1lllIl1l1) -> bool:
        return True

    @classmethod
    def l1lll1l1l1l11lllIl1l1(l1lll1111111ll11Il1l1) -> int:

        return int(10000000000.0)


@dataclass
class ll1lllllll1ll1llIl1l1(lllll111l1l1l1llIl1l1):
    l1lll1ll1lll11llIl1l1 = 'Flask'

    @contextmanager
    def llll11l1111l1ll1Il1l1(ll111ll111ll1lllIl1l1) -> Generator[None, None, None]:




        from flask import Flask as FlaskLib 

        def l11llll1llll1111Il1l1(*l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> Any:
            def llllll11ll11111lIl1l1(l1ll1l1ll1ll1lllIl1l1: Any) -> Any:
                return l1ll1l1ll1ll1lllIl1l1

            return llllll11ll11111lIl1l1

        ll1ll11l111lll1lIl1l1 = FlaskLib.route
        FlaskLib.route = l11llll1llll1111Il1l1  # type: ignore

        try:
            yield 
        finally:
            FlaskLib.route = ll1ll11l111lll1lIl1l1  # type: ignore

    def ll11l1l11l1l1111Il1l1(ll111ll111ll1lllIl1l1) -> List[Type[lll1ll1ll111llllIl1l1]]:
        return [lll1l11l11ll11llIl1l1, l111111llllll11lIl1l1]

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, l1lll1l11111lll1Il1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(l1lll1l11111lll1Il1l1, 'flask.app')):
            ll111ll111ll1lllIl1l1.ll1llllll1111l1lIl1l1()
            ll111ll111ll1lllIl1l1.l11l1l11llll1l1lIl1l1()
            ll111ll111ll1lllIl1l1.ll1111l1111l1lllIl1l1()

        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(l1lll1l11111lll1Il1l1, 'flask.cli')):
            ll111ll111ll1lllIl1l1.l11l1ll1l1ll11l1Il1l1()


    def llll1l1l1l1111l1Il1l1(hostname: Any, port: Any, application: Any, use_reloader: Any = False, use_debugger: Any = False, use_evalex: Any = True, extra_files: Any = None, exclude_patterns: Any = None, reloader_interval: Any = 1, reloader_type: Any = 'auto', threaded: Any = False, processes: Any = 1, request_handler: Any = None, static_files: Any = None, passthrough_errors: Any = False, ssl_context: Any = None) -> Any:
        from typing import cast
        __rw_plugin__ = cast('Flask', globals().get('__rw_plugin__'))

        __rw_plugin__.lll111l1l1l11lllIl1l1 = __rw_plugin__.l11ll1l1111l1ll1Il1l1(port)  # type: ignore
        if (__rw_globals__['env'].page_reload_on_start):  # type: ignore
            __rw_plugin__.lll111l1l1l11lllIl1l1.lllll1l111l1ll1lIl1l1(1.0)  # type: ignore
        __rw_orig__(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)  # type: ignore













    def ll1llllll1111l1lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        try:
            import werkzeug.serving
            import flask.cli
        except ImportError:
            return 

        lll1lllll11ll11lIl1l1.ll1ll11lll1lllllIl1l1(werkzeug.serving.run_simple, ll111ll111ll1lllIl1l1.llll1l1l1l1111l1Il1l1, llllllll1ll11111Il1l1={'__rw_plugin__': ll111ll111ll1lllIl1l1})


    def ll1111l1111l1lllIl1l1(ll111ll111ll1lllIl1l1) -> None:
        try:
            import flask
        except ImportError:
            return 

        llll1lll1ll11l11Il1l1 = flask.app.Flask.__init__

        def l1lllll111l111l1Il1l1(l1lll11ll11llll1Il1l1: Any, *l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> Any:
            llll1lll1ll11l11Il1l1(l1lll11ll11llll1Il1l1, *l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1)
            with ll11l11lll1ll111Il1l1():
                l1lll11ll11llll1Il1l1.config['TEMPLATES_AUTO_RELOAD'] = True

        lll1lllll11ll11lIl1l1.l1111ll1l1l11111Il1l1(flask.app.Flask, '__init__', l1lllll111l111l1Il1l1)

    def l11l1l11llll1l1lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        try:
            import waitress  # type: ignore
        except ImportError:
            return 

        llll1lll1ll11l11Il1l1 = waitress.serve



        def l1lllll111l111l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> Any:
            with ll11l11lll1ll111Il1l1():
                l11lll1llll1l1llIl1l1 = ll1l1lll11l1l11lIl1l1.get('port')
                if ( not l11lll1llll1l1llIl1l1):
                    l11lll1llll1l1llIl1l1 = int(l11111l1111llll1Il1l1[1])

                l11lll1llll1l1llIl1l1 = int(l11lll1llll1l1llIl1l1)

                ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1 = ll111ll111ll1lllIl1l1.l11ll1l1111l1ll1Il1l1(l11lll1llll1l1llIl1l1)
                if (env.page_reload_on_start):
                    ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.lllll1l111l1ll1lIl1l1(1.0)

            llll1lll1ll11l11Il1l1(*l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1)

        lll1lllll11ll11lIl1l1.l1111ll1l1l11111Il1l1(waitress, 'serve', l1lllll111l111l1Il1l1)

    def l11l1ll1l1ll11l1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        try:
            from flask import cli
        except ImportError:
            return 

        l1111ll1l11lll1lIl1l1 = Path(cli.__file__).read_text(encoding='utf-8')
        l1111ll1l11lll1lIl1l1 = l1111ll1l11lll1lIl1l1.replace('.tb_next', '.tb_next.tb_next')

        exec(l1111ll1l11lll1lIl1l1, cli.__dict__)

    def llllll1ll1l111llIl1l1(ll111ll111ll1lllIl1l1) -> None:
        super().llllll1ll1l111llIl1l1()
        import flask.app

        llll1lll1ll11l11Il1l1 = flask.app.Flask.dispatch_request

        def l1lllll111l111l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> Any:
            lll11111l111ll11Il1l1 = llll1lll1ll11l11Il1l1(*l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1)

            if ( not ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
                return lll11111l111ll11Il1l1

            if (isinstance(lll11111l111ll11Il1l1, str)):
                l1l1l11l111111l1Il1l1 = ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.l1ll11l11l1l1lllIl1l1(lll11111l111ll11Il1l1)
                return l1l1l11l111111l1Il1l1
            elif ((isinstance(lll11111l111ll11Il1l1, flask.app.Response) and 'text/html' in lll11111l111ll11Il1l1.content_type)):
                lll11111l111ll11Il1l1.data = ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.l1ll11l11l1l1lllIl1l1(lll11111l111ll11Il1l1.data.decode('utf-8')).encode('utf-8')
                return lll11111l111ll11Il1l1
            else:
                return lll11111l111ll11Il1l1

        flask.app.Flask.dispatch_request = l1lllll111l111l1Il1l1  # type: ignore
