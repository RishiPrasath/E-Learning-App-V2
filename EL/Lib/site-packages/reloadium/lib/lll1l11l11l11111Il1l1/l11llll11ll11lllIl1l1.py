import asyncio
from contextlib import contextmanager
import os
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.l11l11l11111llllIl1l1 import lllllllllll11l1lIl1l1
from reloadium.corium.ll11l1l1111l1111Il1l1 import l1l111l11l1lll11Il1l1
from reloadium.corium.l1llll1llll11l1lIl1l1.l1111ll1l1l11111Il1l1 import lll1lllll11ll11lIl1l1
from reloadium.lib.environ import env
from reloadium.corium.ll111ll1ll11ll1lIl1l1 import ll11l11lll1ll111Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import l11l1l1ll1lllll1Il1l1, l11l11lllllll111Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll1l1ll11lll11l1Il1l1 import lllll111l1l1l1llIl1l1
from reloadium.corium.l11111l1ll1ll111Il1l1 import l1l1l1llll1ll11lIl1l1, ll111l1ll11lllllIl1l1, lll1ll1ll111llllIl1l1, lll11l1ll11l1ll1Il1l1, l111l111l111ll11Il1l1
from reloadium.corium.l1l11l11ll11111lIl1l1 import ll11111l1l1111llIl1l1, l1111l111l1l1l1lIl1l1
from reloadium.corium.lll11ll1ll1111l1Il1l1 import l111ll1l1l11l11lIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1 import lll11ll111ll1l11Il1l1
from dataclasses import dataclass, field


if (TYPE_CHECKING):
    from django.db import transaction
    from django.db.transaction import Atomic


__RELOADIUM__ = True


@dataclass(**l111l111l111ll11Il1l1)
class l1l11ll111l111l1Il1l1(lll11l1ll11l1ll1Il1l1):
    ll1l11lll1111l11Il1l1 = 'Field'

    @classmethod
    def l11l1lllll111111Il1l1(l1lll1111111ll11Il1l1, ll1lll11lll11lllIl1l1: l111ll1l1l11l11lIl1l1.l111ll111llll111Il1l1, lll1l11lll1lllllIl1l1: Any, llll1ll1l111lll1Il1l1: ll111l1ll11lllllIl1l1) -> bool:
        from django.db.models.fields import Field

        if ((hasattr(lll1l11lll1lllllIl1l1, 'field') and isinstance(lll1l11lll1lllllIl1l1.field, Field))):
            return True

        return False

    def lllllllllll11l11Il1l1(ll111ll111ll1lllIl1l1, ll111l1llll1l11lIl1l1: lll1ll1ll111llllIl1l1) -> bool:
        return True

    @classmethod
    def l1lll1l1l1l11lllIl1l1(l1lll1111111ll11Il1l1) -> int:
        return 200


@dataclass(repr=False)
class l1llll111l111l11Il1l1(l11l1l1ll1lllll1Il1l1):
    l11111ll1l1111llIl1l1: "Atomic" = field(init=False)

    l11ll111ll11l11lIl1l1: bool = field(init=False, default=False)

    def lll1lllllllll11lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        super().lll1lllllllll11lIl1l1()
        from django.db import transaction

        ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1 = transaction.atomic()
        ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__enter__()

    def l11111l11l1l11l1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l11111l11l1l11l1Il1l1()
        if (ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1 = True
        from django.db import transaction

        transaction.set_rollback(True)
        ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__exit__(None, None, None)

    def l1llll11l1ll1l11Il1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l1llll11l1ll1l11Il1l1()

        if (ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1 = True
        ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__exit__(None, None, None)

    def __repr__(ll111ll111ll1lllIl1l1) -> str:
        return 'DbMemento'


@dataclass(repr=False)
class ll1llll1ll11llllIl1l1(l11l11lllllll111Il1l1):
    l11111ll1l1111llIl1l1: "Atomic" = field(init=False)

    l11ll111ll11l11lIl1l1: bool = field(init=False, default=False)

    async def lll1lllllllll11lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        await super().lll1lllllllll11lIl1l1()
        from django.db import transaction
        from asgiref.sync import sync_to_async

        ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1 = transaction.atomic()


        with lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.ll1ll11ll1ll1111Il1l1.l1ll111lll1l1l11Il1l1(False):
            await sync_to_async(ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__enter__)()

    async def l11111l11l1l11l1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().l11111l11l1l11l1Il1l1()
        if (ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1 = True
        from django.db import transaction

        def llllllll11l1l1l1Il1l1() -> None:
            transaction.set_rollback(True)
            ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__exit__(None, None, None)
        with lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.ll1ll11ll1ll1111Il1l1.l1ll111lll1l1l11Il1l1(False):
            await sync_to_async(llllllll11l1l1l1Il1l1)()

    async def l1llll11l1ll1l11Il1l1(ll111ll111ll1lllIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().l1llll11l1ll1l11Il1l1()

        if (ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l11ll111ll11l11lIl1l1 = True
        with lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.ll1ll11ll1ll1111Il1l1.l1ll111lll1l1l11Il1l1(False):
            await sync_to_async(ll111ll111ll1lllIl1l1.l11111ll1l1111llIl1l1.__exit__)(None, None, None)

    def __repr__(ll111ll111ll1lllIl1l1) -> str:
        return 'AsyncDbMemento'


@dataclass
class l1ll1llll111111lIl1l1(lllll111l1l1l1llIl1l1):
    l1lll1ll1lll11llIl1l1 = 'Django'

    lll11llll111ll11Il1l1: Optional[int] = field(init=False)
    l1lll11l1l11l11lIl1l1: Optional[Callable[..., Any]] = field(init=False, default=None)

    llll11lll11l11llIl1l1: Any = field(init=False, default=None)
    ll1l11l11l11l11lIl1l1: Any = field(init=False, default=None)
    lllll1llll1llll1Il1l1: Any = field(init=False, default=None)

    ll1l1ll1111l1111Il1l1 = True

    def __post_init__(ll111ll111ll1lllIl1l1) -> None:
        super().__post_init__()
        ll111ll111ll1lllIl1l1.lll11llll111ll11Il1l1 = None

    def ll11l1l11l1l1111Il1l1(ll111ll111ll1lllIl1l1) -> List[Type[lll1ll1ll111llllIl1l1]]:
        return [l1l11ll111l111l1Il1l1]

    def l11l1l111l111111Il1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l11l1l111l111111Il1l1()
        if ('runserver' in sys.argv):
            sys.argv.append('--noreload')

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'django.core.management.commands.runserver')):
            ll111ll111ll1lllIl1l1.ll1l111ll1ll1111Il1l1()
            if ( not ll111ll111ll1lllIl1l1.llllll1l11llll11Il1l1):
                ll111ll111ll1lllIl1l1.l1lll111lll1llllIl1l1()

    def l1llllll1l1lll1lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        import django.core.management.commands.runserver

        django.core.management.commands.runserver.Command.handle = ll111ll111ll1lllIl1l1.llll11lll11l11llIl1l1
        django.core.management.commands.runserver.Command.get_handler = ll111ll111ll1lllIl1l1.lllll1llll1llll1Il1l1
        django.core.handlers.base.BaseHandler.get_response = ll111ll111ll1lllIl1l1.ll1l11l11l11l11lIl1l1

    def ll1ll111111l1ll1Il1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str, l1lll1111l1lll1lIl1l1: bool) -> Optional["ll11111l1l1111llIl1l1"]:
        if (ll111ll111ll1lllIl1l1.llllll1l11llll11Il1l1):
            return None

        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        if (l1lll1111l1lll1lIl1l1):
            return None
        else:
            l1l1l11l111111l1Il1l1 = l1llll111l111l11Il1l1(lll111ll111ll1l1Il1l1=lll111ll111ll1l1Il1l1, ll11l1lll1llll11Il1l1=ll111ll111ll1lllIl1l1)
            l1l1l11l111111l1Il1l1.lll1lllllllll11lIl1l1()

        return l1l1l11l111111l1Il1l1

    async def l111l1ll11llllllIl1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str) -> Optional["l1111l111l1l1l1lIl1l1"]:
        if (ll111ll111ll1lllIl1l1.llllll1l11llll11Il1l1):
            return None

        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        l1l1l11l111111l1Il1l1 = ll1llll1ll11llllIl1l1(lll111ll111ll1l1Il1l1=lll111ll111ll1l1Il1l1, ll11l1lll1llll11Il1l1=ll111ll111ll1lllIl1l1)
        await l1l1l11l111111l1Il1l1.lll1lllllllll11lIl1l1()
        return l1l1l11l111111l1Il1l1

    def ll1l111ll1ll1111Il1l1(ll111ll111ll1lllIl1l1) -> None:
        import django.core.management.commands.runserver

        ll111ll111ll1lllIl1l1.llll11lll11l11llIl1l1 = django.core.management.commands.runserver.Command.handle

        def l1lllll111l111l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1lllll1llll111Il1l1: Any) -> Any:
            with ll11l11lll1ll111Il1l1():
                l11lll1llll1l1llIl1l1 = ll1lllll1llll111Il1l1.get('addrport')
                if ( not l11lll1llll1l1llIl1l1):
                    l11lll1llll1l1llIl1l1 = django.core.management.commands.runserver.Command.default_port

                l11lll1llll1l1llIl1l1 = l11lll1llll1l1llIl1l1.split(':')[ - 1]
                l11lll1llll1l1llIl1l1 = int(l11lll1llll1l1llIl1l1)
                ll111ll111ll1lllIl1l1.lll11llll111ll11Il1l1 = l11lll1llll1l1llIl1l1

            return ll111ll111ll1lllIl1l1.llll11lll11l11llIl1l1(*l11111l1111llll1Il1l1, **ll1lllll1llll111Il1l1)

        lll1lllll11ll11lIl1l1.l1111ll1l1l11111Il1l1(django.core.management.commands.runserver.Command, 'handle', l1lllll111l111l1Il1l1)

    def l1lll111lll1llllIl1l1(ll111ll111ll1lllIl1l1) -> None:
        import django.core.management.commands.runserver

        ll111ll111ll1lllIl1l1.lllll1llll1llll1Il1l1 = django.core.management.commands.runserver.Command.get_handler

        def l1lllll111l111l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1lllll1llll111Il1l1: Any) -> Any:
            with ll11l11lll1ll111Il1l1():
                assert ll111ll111ll1lllIl1l1.lll11llll111ll11Il1l1
                ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1 = ll111ll111ll1lllIl1l1.l11ll1l1111l1ll1Il1l1(ll111ll111ll1lllIl1l1.lll11llll111ll11Il1l1)
                if (env.page_reload_on_start):
                    ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.lllll1l111l1ll1lIl1l1(2.0)

            return ll111ll111ll1lllIl1l1.lllll1llll1llll1Il1l1(*l11111l1111llll1Il1l1, **ll1lllll1llll111Il1l1)

        lll1lllll11ll11lIl1l1.l1111ll1l1l11111Il1l1(django.core.management.commands.runserver.Command, 'get_handler', l1lllll111l111l1Il1l1)

    def llllll1ll1l111llIl1l1(ll111ll111ll1lllIl1l1) -> None:
        super().llllll1ll1l111llIl1l1()

        import django.core.handlers.base

        ll111ll111ll1lllIl1l1.ll1l11l11l11l11lIl1l1 = django.core.handlers.base.BaseHandler.get_response

        def l1lllll111l111l1Il1l1(ll11l111ll1l1111Il1l1: Any, ll1ll1111ll1ll11Il1l1: Any) -> Any:
            lll11111l111ll11Il1l1 = ll111ll111ll1lllIl1l1.ll1l11l11l11l11lIl1l1(ll11l111ll1l1111Il1l1, ll1ll1111ll1ll11Il1l1)

            if ( not ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
                return lll11111l111ll11Il1l1

            l111l1lll1l1lll1Il1l1 = lll11111l111ll11Il1l1.get('content-type')

            if (( not l111l1lll1l1lll1Il1l1 or 'text/html' not in l111l1lll1l1lll1Il1l1)):
                return lll11111l111ll11Il1l1

            l1111lll1111l11lIl1l1 = lll11111l111ll11Il1l1.content

            if (isinstance(l1111lll1111l11lIl1l1, bytes)):
                l1111lll1111l11lIl1l1 = l1111lll1111l11lIl1l1.decode('utf-8')

            l1lllllll111l11lIl1l1 = ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.l1ll11l11l1l1lllIl1l1(l1111lll1111l11lIl1l1)

            lll11111l111ll11Il1l1.content = l1lllllll111l11lIl1l1.encode('utf-8')
            lll11111l111ll11Il1l1['content-length'] = str(len(lll11111l111ll11Il1l1.content)).encode('ascii')
            return lll11111l111ll11Il1l1

        django.core.handlers.base.BaseHandler.get_response = l1lllll111l111l1Il1l1  # type: ignore

    def lll1llll1lll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        super().lll1llll1lll11llIl1l1(ll11l11111l1ll11Il1l1)

        from django.apps.registry import Apps

        ll111ll111ll1lllIl1l1.l1lll11l1l11l11lIl1l1 = Apps.register_model

        def l111l1llll1ll1l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> Any:
            pass

        Apps.register_model = l111l1llll1ll1l1Il1l1

    def l1l11l1llll11l11Il1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path, l1l1l111llllll1lIl1l1: List[l1l1l1llll1ll11lIl1l1]) -> None:
        super().l1l11l1llll11l11Il1l1(ll11l11111l1ll11Il1l1, l1l1l111llllll1lIl1l1)

        if ( not ll111ll111ll1lllIl1l1.l1lll11l1l11l11lIl1l1):
            return 

        from django.apps.registry import Apps

        Apps.register_model = ll111ll111ll1lllIl1l1.l1lll11l1l11l11lIl1l1
