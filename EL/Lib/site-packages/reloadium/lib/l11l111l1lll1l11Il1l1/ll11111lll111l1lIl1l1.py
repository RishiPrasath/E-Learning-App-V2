from pathlib import Path
import sys
import threading
from types import CodeType, FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, cast

from reloadium.corium import l111l111ll11111lIl1l1, ll111ll1ll11ll1lIl1l1, public, l1l1111llllll1l1Il1l1, l1llll1llll11l1lIl1l1
from reloadium.corium.l1ll1lll1l11ll11Il1l1 import llll1111llllll1lIl1l1, l1l1ll111111lll1Il1l1
from reloadium.corium.ll111ll1ll11ll1lIl1l1 import l1l1lll1lllll111Il1l1, ll11l11lll1ll111Il1l1, ll111l111l111ll1Il1l1
from reloadium.corium.l11l11l11111llllIl1l1 import lllllllllll11l1lIl1l1
from reloadium.corium.llll1ll111111lllIl1l1 import llll1ll111111lllIl1l1
from reloadium.corium.l111l1l11ll111l1Il1l1 import l1ll11111lllllllIl1l1
from reloadium.corium.l1l11l11ll11111lIl1l1 import ll11111l1l1111llIl1l1, l1111l111l1l1l1lIl1l1
from dataclasses import dataclass, field


__RELOADIUM__ = True

__all__ = ['lllll111lll1l1llIl1l1', 'l111l1lll1l11lllIl1l1', 'lll1l11lll11lll1Il1l1']


l1ll11l111l11ll1Il1l1 = llll1ll111111lllIl1l1.l11ll1l1ll111111Il1l1(__name__)


class lllll111lll1l1llIl1l1:
    @classmethod
    def lll11l111ll111l1Il1l1(ll111ll111ll1lllIl1l1) -> Optional[FrameType]:
        ll111lll1l1l11llIl1l1: FrameType = sys._getframe(2)
        l1l1l11l111111l1Il1l1 = next(l1llll1llll11l1lIl1l1.ll111lll1l1l11llIl1l1.l1l1ll11l1l11l1lIl1l1(ll111lll1l1l11llIl1l1))
        return l1l1l11l111111l1Il1l1


class l111l1lll1l11lllIl1l1(lllll111lll1l1llIl1l1):
    @classmethod
    def llll1l1111l11lllIl1l1(l1lll1111111ll11Il1l1, l11111l1111llll1Il1l1: List[Any], ll1l1lll11l1l11lIl1l1: Dict[str, Any], l11l1ll1l1l111llIl1l1: List[ll11111l1l1111llIl1l1]) -> Any:  # type: ignore
        with ll11l11lll1ll111Il1l1():
            assert lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1
            ll111lll1l1l11llIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1.ll1l1l1ll1lll11lIl1l1.lll11l1ll11lllllIl1l1()
            ll111lll1l1l11llIl1l1.lll1l1l1l11l11llIl1l1()

            ll11llllllll111lIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.llll111lllllll1lIl1l1.l1llll1ll111l1l1Il1l1(ll111lll1l1l11llIl1l1.l111l1ll111llll1Il1l1, ll111lll1l1l11llIl1l1.ll1111llll11l11lIl1l1.l11lll11ll11l1llIl1l1())
            assert ll11llllllll111lIl1l1
            ll1l1ll11ll1111lIl1l1 = l1lll1111111ll11Il1l1.lll11l111ll111l1Il1l1()

            for l1l11l11l111111lIl1l1 in l11l1ll1l1l111llIl1l1:
                l1l11l11l111111lIl1l1.l11111l11l1l11l1Il1l1()

            for l1l11l11l111111lIl1l1 in l11l1ll1l1l111llIl1l1:
                l1l11l11l111111lIl1l1.l1llll11l1ll1l11Il1l1()


        l1l1l11l111111l1Il1l1 = ll11llllllll111lIl1l1(*l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1);        ll111lll1l1l11llIl1l1.l11lll111l11ll1lIl1l1.additional_info.pydev_step_stop = ll1l1ll11ll1111lIl1l1  # type: ignore

        return l1l1l11l111111l1Il1l1

    @classmethod
    async def lll11l1l1lll1lllIl1l1(l1lll1111111ll11Il1l1, l11111l1111llll1Il1l1: List[Any], ll1l1lll11l1l11lIl1l1: Dict[str, Any], l11l1ll1l1l111llIl1l1: List[l1111l111l1l1l1lIl1l1]) -> Any:  # type: ignore
        with ll11l11lll1ll111Il1l1():
            assert lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1
            ll111lll1l1l11llIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1.ll1l1l1ll1lll11lIl1l1.lll11l1ll11lllllIl1l1()
            ll111lll1l1l11llIl1l1.lll1l1l1l11l11llIl1l1()

            ll11llllllll111lIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.llll111lllllll1lIl1l1.l1llll1ll111l1l1Il1l1(ll111lll1l1l11llIl1l1.l111l1ll111llll1Il1l1, ll111lll1l1l11llIl1l1.ll1111llll11l11lIl1l1.l11lll11ll11l1llIl1l1())
            assert ll11llllllll111lIl1l1
            ll1l1ll11ll1111lIl1l1 = l1lll1111111ll11Il1l1.lll11l111ll111l1Il1l1()

            for l1l11l11l111111lIl1l1 in l11l1ll1l1l111llIl1l1:
                await l1l11l11l111111lIl1l1.l11111l11l1l11l1Il1l1()

            for l1l11l11l111111lIl1l1 in l11l1ll1l1l111llIl1l1:
                await l1l11l11l111111lIl1l1.l1llll11l1ll1l11Il1l1()


        l1l1l11l111111l1Il1l1 = await ll11llllllll111lIl1l1(*l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1);        ll111lll1l1l11llIl1l1.l11lll111l11ll1lIl1l1.additional_info.pydev_step_stop = ll1l1ll11ll1111lIl1l1  # type: ignore

        return l1l1l11l111111l1Il1l1


class lll1l11lll11lll1Il1l1(lllll111lll1l1llIl1l1):
    @classmethod
    def llll1l1111l11lllIl1l1(l1lll1111111ll11Il1l1) -> Optional[ModuleType]:  # type: ignore
        with ll11l11lll1ll111Il1l1():
            assert lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1
            ll111lll1l1l11llIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11l111l1lll1l11Il1l1.ll1l1l1ll1lll11lIl1l1.lll11l1ll11lllllIl1l1()

            l1ll111l1l1ll111Il1l1 = Path(ll111lll1l1l11llIl1l1.lll1l11lll1lllllIl1l1.f_globals['__spec__'].origin).absolute()
            l11l1ll11lll1ll1Il1l1 = ll111lll1l1l11llIl1l1.lll1l11lll1lllllIl1l1.f_globals['__name__']
            ll111lll1l1l11llIl1l1.lll1l1l1l11l11llIl1l1()
            lllll1111l1lll1lIl1l1 = lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.lllll1l1lll11ll1Il1l1.l1111llll1111l11Il1l1(l1ll111l1l1ll111Il1l1)

            if ( not lllll1111l1lll1lIl1l1):
                l1ll11l111l11ll1Il1l1.ll1l1l1ll1l11111Il1l1('Could not retrieve src.', l11ll11l11lll111Il1l1={'file': l1ll11111lllllllIl1l1.ll11l11111l1ll11Il1l1(l1ll111l1l1ll111Il1l1), 
'fullname': l1ll11111lllllllIl1l1.l11l1ll11lll1ll1Il1l1(l11l1ll11lll1ll1Il1l1)})

            assert lllll1111l1lll1lIl1l1

        try:
            lllll1111l1lll1lIl1l1.l1l111lll11l111lIl1l1()
            lllll1111l1lll1lIl1l1.l1111l1l111lll11Il1l1(ll1ll11llll11lllIl1l1=False)
            lllll1111l1lll1lIl1l1.l1ll111l1111llllIl1l1(ll1ll11llll11lllIl1l1=False)
        except l1l1lll1lllll111Il1l1 as l11l11l11111l1llIl1l1:
            ll111lll1l1l11llIl1l1.llllll1l1ll1lll1Il1l1(l11l11l11111l1llIl1l1)
            return None

        import importlib.util

        lll111ll1111lll1Il1l1 = ll111lll1l1l11llIl1l1.lll1l11lll1lllllIl1l1.f_locals['__spec__']
        ll1ll111ll1l11llIl1l1 = importlib.util.module_from_spec(lll111ll1111lll1Il1l1)

        lllll1111l1lll1lIl1l1.ll1l1l1l111llll1Il1l1(ll1ll111ll1l11llIl1l1)
        return ll1ll111ll1l11llIl1l1


l1l1ll111111lll1Il1l1.l1l111ll1llll1l1Il1l1(llll1111llllll1lIl1l1.lllllll1ll1111llIl1l1, l111l1lll1l11lllIl1l1.llll1l1111l11lllIl1l1)
l1l1ll111111lll1Il1l1.l1l111ll1llll1l1Il1l1(llll1111llllll1lIl1l1.l1ll11l11l11ll11Il1l1, l111l1lll1l11lllIl1l1.lll11l1l1lll1lllIl1l1)
l1l1ll111111lll1Il1l1.l1l111ll1llll1l1Il1l1(llll1111llllll1lIl1l1.lll1ll1ll11ll11lIl1l1, lll1l11lll11lll1Il1l1.llll1l1111l11lllIl1l1)
