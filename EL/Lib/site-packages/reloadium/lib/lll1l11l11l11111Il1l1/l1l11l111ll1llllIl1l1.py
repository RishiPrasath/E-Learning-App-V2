import re
from contextlib import contextmanager
import os
import sys
import types
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Union

from reloadium.corium.ll111ll1ll11ll1lIl1l1 import ll11l11lll1ll111Il1l1
from reloadium.corium.l1llll1llll11l1lIl1l1.l1111ll1l1l11111Il1l1 import lll1lllll11ll11lIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1, l11l1l1ll1lllll1Il1l1
from reloadium.corium.l1l11l11ll11111lIl1l1 import ll11111l1l1111llIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1 import lll11ll111ll1l11Il1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from sqlalchemy.engine.base import Engine, Transaction
    from sqlalchemy.orm.session import Session


__RELOADIUM__ = True


@dataclass(repr=False)
class l1llll111l111l11Il1l1(l11l1l1ll1lllll1Il1l1):
    ll11l1lll1llll11Il1l1: "l1l1l1lll11ll1llIl1l1"
    llllllllll1l11l1Il1l1: List["Transaction"] = field(init=False, default_factory=list)

    def lll1lllllllll11lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        from sqlalchemy.orm.session import _sessions

        super().lll1lllllllll11lIl1l1()

        ll1llllllll1111lIl1l1 = list(_sessions.values())

        for ll111ll11lll1l11Il1l1 in ll1llllllll1111lIl1l1:
            if ( not ll111ll11lll1l11Il1l1.is_active):
                continue

            l11l1l1111lll1l1Il1l1 = ll111ll11lll1l11Il1l1.begin_nested()
            ll111ll111ll1lllIl1l1.llllllllll1l11l1Il1l1.append(l11l1l1111lll1l1Il1l1)

    def __repr__(ll111ll111ll1lllIl1l1) -> str:
        return 'DbMemento'

    def l11111l11l1l11l1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l11111l11l1l11l1Il1l1()

        while ll111ll111ll1lllIl1l1.llllllllll1l11l1Il1l1:
            l11l1l1111lll1l1Il1l1 = ll111ll111ll1lllIl1l1.llllllllll1l11l1Il1l1.pop()
            if (l11l1l1111lll1l1Il1l1.is_active):
                try:
                    l11l1l1111lll1l1Il1l1.rollback()
                except :
                    pass

    def l1llll11l1ll1l11Il1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l1llll11l1ll1l11Il1l1()

        while ll111ll111ll1lllIl1l1.llllllllll1l11l1Il1l1:
            l11l1l1111lll1l1Il1l1 = ll111ll111ll1lllIl1l1.llllllllll1l11l1Il1l1.pop()
            if (l11l1l1111lll1l1Il1l1.is_active):
                try:
                    l11l1l1111lll1l1Il1l1.commit()
                except :
                    pass


@dataclass
class l1l1l1lll11ll1llIl1l1(lll1l11111l11111Il1l1):
    l1lll1ll1lll11llIl1l1 = 'Sqlalchemy'

    l111l111l1l111llIl1l1: List["Engine"] = field(init=False, default_factory=list)
    ll1llllllll1111lIl1l1: Set["Session"] = field(init=False, default_factory=set)
    lll111ll1l11ll1lIl1l1: Tuple[int, ...] = field(init=False)

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'sqlalchemy')):
            ll111ll111ll1lllIl1l1.l1ll1llllll1l111Il1l1(ll1ll111ll1l11llIl1l1)

        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'sqlalchemy.engine.base')):
            ll111ll111ll1lllIl1l1.l1ll11ll11111lllIl1l1(ll1ll111ll1l11llIl1l1)

    def l1ll1llllll1l111Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: Any) -> None:
        l1111lll1111l11lIl1l1 = Path(ll1ll111ll1l11llIl1l1.__file__).read_text(encoding='utf-8')
        __version__ = re.findall('__version__\\s*?=\\s*?"(.*?)"', l1111lll1111l11lIl1l1)[0]

        l1ll11l1111lllllIl1l1 = [int(lll111ll1llllll1Il1l1) for lll111ll1llllll1Il1l1 in __version__.split('.')]
        ll111ll111ll1lllIl1l1.lll111ll1l11ll1lIl1l1 = tuple(l1ll11l1111lllllIl1l1)

    def ll1ll111111l1ll1Il1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str, l1lll1111l1lll1lIl1l1: bool) -> Optional["ll11111l1l1111llIl1l1"]:
        l1l1l11l111111l1Il1l1 = l1llll111l111l11Il1l1(lll111ll111ll1l1Il1l1=lll111ll111ll1l1Il1l1, ll11l1lll1llll11Il1l1=ll111ll111ll1lllIl1l1)
        l1l1l11l111111l1Il1l1.lll1lllllllll11lIl1l1()
        return l1l1l11l111111l1Il1l1

    def l1ll11ll11111lllIl1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: Any) -> None:
        lll1llll1l1111l1Il1l1 = locals().copy()

        lll1llll1l1111l1Il1l1.update({'original': ll1ll111ll1l11llIl1l1.Engine.__init__, 'reloader_code': ll11l11lll1ll111Il1l1, 'engines': ll111ll111ll1lllIl1l1.l111l111l1l111llIl1l1})





        ll1l1l1ll11l11llIl1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    proxy: Any = None,\n                    execution_options: Any = None,\n                    hide_parameters: Any = None,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         proxy,\n                         execution_options,\n                         hide_parameters\n                         )\n                with reloader_code():\n                    engines.append(self2)')
























        lll11ll11111ll1lIl1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    query_cache_size: Any = 500,\n                    execution_options: Any = None,\n                    hide_parameters: Any = False,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         query_cache_size,\n                         execution_options,\n                         hide_parameters)\n                with reloader_code():\n                    engines.append(self2)\n        ')
























        if (ll111ll111ll1lllIl1l1.lll111ll1l11ll1lIl1l1 <= (1, 3, 24, )):
            exec(ll1l1l1ll11l11llIl1l1, {**globals(), **lll1llll1l1111l1Il1l1}, lll1llll1l1111l1Il1l1)
        else:
            exec(lll11ll11111ll1lIl1l1, {**globals(), **lll1llll1l1111l1Il1l1}, lll1llll1l1111l1Il1l1)

        lll1lllll11ll11lIl1l1.l1111ll1l1l11111Il1l1(ll1ll111ll1l11llIl1l1.Engine, '__init__', lll1llll1l1111l1Il1l1['patched'])
