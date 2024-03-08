from contextlib import contextmanager
from pathlib import Path
import sys
import types
from threading import Timer, Thread
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type, Set


import reloadium.lib.lll1l11l11l11111Il1l1.lllll11l1111llllIl1l1
from reloadium.corium import l1l1ll1l11lll1l1Il1l1, l111l111ll11111lIl1l1, l1llll1llll11l1lIl1l1
from reloadium.corium.ll111l11l111111lIl1l1 import ll111111ll111l1lIl1l1
from reloadium.corium.ll11l1l1111l1111Il1l1 import l1ll1lllll111l1lIl1l1, ll1l1lll1l1ll11lIl1l1
from reloadium.corium.l1l1111llllll1l1Il1l1 import ll111ll1l1l11l1lIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1.l11lll111l11ll1lIl1l1 import ll11111lll11ll1lIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.l11llll11ll11lllIl1l1 import l1ll1llll111111lIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.l1l1l1lllll1l111Il1l1 import l1l11l1l1lll1l11Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.l11llllllll11lllIl1l1 import ll1lllllll1ll1llIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.llll1lllll1lll1lIl1l1 import ll11l11l11111l11Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.lll11lll11ll1l11Il1l1 import ll1ll11lll11ll11Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.lll11l11l1l1ll1lIl1l1 import lllll1111l11l1llIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll1lll11l11l1111Il1l1 import l11111l1lll1ll11Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.lll111lll1lll1l1Il1l1 import ll1l1llll11l111lIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.l1l11l111ll1llllIl1l1 import l1l1l1lll11ll1llIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll1l1l11l1l11111Il1l1 import ll1l1l1ll111111lIl1l1
from reloadium.corium.llll1ll111111lllIl1l1 import llll1ll111111lllIl1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.corium.l1l1l1l1l111111lIl1l1 import l11l1ll1l11ll11lIl1l1
    from reloadium.corium.l11111l1ll1ll111Il1l1 import l1l1l1llll1ll11lIl1l1


__RELOADIUM__ = True

l1ll11l111l11ll1Il1l1 = llll1ll111111lllIl1l1.l11ll1l1ll111111Il1l1(__name__)


@dataclass
class ll11llllll11l111Il1l1:
    l1l1l1l1l111111lIl1l1: "l11l1ll1l11ll11lIl1l1"

    lll1l11l11l11111Il1l1: List[lll1l11111l11111Il1l1] = field(init=False, default_factory=list)

    ll1l11l1ll1l1lllIl1l1: List[types.ModuleType] = field(init=False, default_factory=list)

    lll111lll1l1111lIl1l1: List[Type[lll1l11111l11111Il1l1]] = field(init=False, default_factory=lambda :[ll1lllllll1ll1llIl1l1, lllll1111l11l1llIl1l1, l1ll1llll111111lIl1l1, l1l1l1lll11ll1llIl1l1, l11111l1lll1ll11Il1l1, ll11l11l11111l11Il1l1, ll1l1llll11l111lIl1l1, ll1l1l1ll111111lIl1l1, l1l11l1l1lll1l11Il1l1, ll1ll11lll11ll11Il1l1])




    lllll11llll1ll1lIl1l1: List[Type[lll1l11111l11111Il1l1]] = field(init=False, default_factory=list)
    ll1l11l1l11l1ll1Il1l1 = (1 if ll111111ll111l1lIl1l1().l11ll1l11ll1l1llIl1l1 in [ll111ll1l1l11l1lIl1l1.ll111lll11ll1l11Il1l1, ll111ll1l1l11l1lIl1l1.lll1lll111111lllIl1l1] else 5)

    def __post_init__(ll111ll111ll1lllIl1l1) -> None:
        if (ll111111ll111l1lIl1l1().l1l1l1l1l11ll11lIl1l1.l11ll11l11l1l1llIl1l1):
            ll111ll111ll1lllIl1l1.lll111lll1l1111lIl1l1.remove(ll1l1llll11l111lIl1l1)

        ll11111lll11ll1lIl1l1(ll11l11l1l11ll11Il1l1=ll111ll111ll1lllIl1l1.l11lll111l11l1l1Il1l1, lll111ll111ll1l1Il1l1='show-forbidden-dialog').start()

    def l11lll111l11l1l1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        l1llll1llll11l1lIl1l1.lll11ll111ll1l11Il1l1.ll11lll11l1lllllIl1l1(ll111ll111ll1lllIl1l1.ll1l11l1l11l1ll1Il1l1)

        ll111ll111ll1lllIl1l1.l1l1l1l1l111111lIl1l1.lll1ll111l1111l1Il1l1.l1l1lll1l1l11111Il1l1()

        if ( not ll111ll111ll1lllIl1l1.lllll11llll1ll1lIl1l1):
            return 

        lll1l11l11l11111Il1l1 = [l11l11l11111l1llIl1l1.l1lll1ll1lll11llIl1l1 for l11l11l11111l1llIl1l1 in ll111ll111ll1lllIl1l1.lllll11llll1ll1lIl1l1]
        ll111ll111ll1lllIl1l1.l1l1l1l1l111111lIl1l1.ll1l111l1llll1llIl1l1.lll1l1lllllll111Il1l1(ll1l1lll1l1ll11lIl1l1.l111ll11l111l111Il1l1, l111l111ll11111lIl1l1.ll11lll1lll11lllIl1l1.l1ll1l11l1lll1llIl1l1(lll1l11l11l11111Il1l1), 
l1lll11111l111l1Il1l1='')

    def lll1lll1ll11l1llIl1l1(ll111ll111ll1lllIl1l1, l1lll11l1lll1lllIl1l1: types.ModuleType) -> None:
        for ll1lll1111111111Il1l1 in ll111ll111ll1lllIl1l1.lll111lll1l1111lIl1l1.copy():
            if (ll1lll1111111111Il1l1.l1ll11llll11111lIl1l1(l1lll11l1lll1lllIl1l1)):
                if (( not ll1lll1111111111Il1l1.ll1l1ll1111l1111Il1l1 and ll111ll111ll1lllIl1l1.l1l1l1l1l111111lIl1l1.ll1l111l1llll1llIl1l1.ll11l1l1111l1111Il1l1.ll1l11ll1llllll1Il1l1([ll1lll1111111111Il1l1.l1lll1ll1lll11llIl1l1]) is False)):
                    ll111ll111ll1lllIl1l1.lllll11llll1ll1lIl1l1.append(ll1lll1111111111Il1l1)
                    ll111ll111ll1lllIl1l1.lll111lll1l1111lIl1l1.remove(ll1lll1111111111Il1l1)
                    continue
                ll111ll111ll1lllIl1l1.ll1111ll1l11l11lIl1l1(ll1lll1111111111Il1l1)

        if (l1lll11l1lll1lllIl1l1 in ll111ll111ll1lllIl1l1.ll1l11l1ll1l1lllIl1l1):
            return 

        for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy():
            l11l1l1l1llll11lIl1l1.l111ll1ll1l1l1l1Il1l1(l1lll11l1lll1lllIl1l1)

        ll111ll111ll1lllIl1l1.ll1l11l1ll1l1lllIl1l1.append(l1lll11l1lll1lllIl1l1)

    def ll1111ll1l11l11lIl1l1(ll111ll111ll1lllIl1l1, ll1lll1111111111Il1l1: Type[lll1l11111l11111Il1l1]) -> None:
        ll1l111ll1ll11llIl1l1 = ll1lll1111111111Il1l1(ll111ll111ll1lllIl1l1, ll111ll111ll1lllIl1l1.l1l1l1l1l111111lIl1l1.ll1l111l1llll1llIl1l1.ll11l1l1111l1111Il1l1)

        ll111ll111ll1lllIl1l1.l1l1l1l1l111111lIl1l1.l1l1ll1lll11llllIl1l1.l1ll111111l1l11lIl1l1.ll1lll1l11ll1l1lIl1l1(l1l1ll1l11lll1l1Il1l1.l11ll1l111ll1l1lIl1l1(ll1l111ll1ll11llIl1l1))
        ll1l111ll1ll11llIl1l1.l11l1l111l111111Il1l1()
        ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.append(ll1l111ll1ll11llIl1l1)

        if (ll1lll1111111111Il1l1 in ll111ll111ll1lllIl1l1.lll111lll1l1111lIl1l1):
            ll111ll111ll1lllIl1l1.lll111lll1l1111lIl1l1.remove(ll1lll1111111111Il1l1)

    @contextmanager
    def llll11l1111l1ll1Il1l1(ll111ll111ll1lllIl1l1) -> Generator[None, None, None]:
        l111ll11111l1ll1Il1l1 = [l11l1l1l1llll11lIl1l1.llll11l1111l1ll1Il1l1() for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy()]

        for lll11ll1ll1l1111Il1l1 in l111ll11111l1ll1Il1l1:
            lll11ll1ll1l1111Il1l1.__enter__()

        yield 

        for lll11ll1ll1l1111Il1l1 in l111ll11111l1ll1Il1l1:
            lll11ll1ll1l1111Il1l1.__exit__(*sys.exc_info())

    def lll1llll1lll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy():
            l11l1l1l1llll11lIl1l1.lll1llll1lll11llIl1l1(ll11l11111l1ll11Il1l1)

    def ll1111l1l1ll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy():
            l11l1l1l1llll11lIl1l1.ll1111l1l1ll11llIl1l1(ll11l11111l1ll11Il1l1)

    def ll1l1l1l11l111l1Il1l1(ll111ll111ll1lllIl1l1, l1111l1ll111l111Il1l1: Exception) -> None:
        for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy():
            l11l1l1l1llll11lIl1l1.ll1l1l1l11l111l1Il1l1(l1111l1ll111l111Il1l1)

    def l1l11l1llll11l11Il1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path, l1l1l111llllll1lIl1l1: List["l1l1l1llll1ll11lIl1l1"]) -> None:
        for l11l1l1l1llll11lIl1l1 in ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.copy():
            l11l1l1l1llll11lIl1l1.l1l11l1llll11l11Il1l1(ll11l11111l1ll11Il1l1, l1l1l111llllll1lIl1l1)

    def l1lll1l1llll1lllIl1l1(ll111ll111ll1lllIl1l1) -> None:
        ll111ll111ll1lllIl1l1.lll1l11l11l11111Il1l1.clear()
