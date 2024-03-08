from abc import ABC
from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.ll11l1l1111l1111Il1l1 import l1ll1lllll111l1lIl1l1, l1l111l11l1lll11Il1l1
from reloadium.corium.llll1ll111111lllIl1l1 import ll1l11ll1ll1llllIl1l1, llll1ll111111lllIl1l1
from reloadium.corium.l11111l1ll1ll111Il1l1 import l1l1l1llll1ll11lIl1l1, lll1ll1ll111llllIl1l1
from reloadium.corium.l1l11l11ll11111lIl1l1 import ll11111l1l1111llIl1l1, l1111l111l1l1l1lIl1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.lib.lll1l11l11l11111Il1l1.l1llll11lllllll1Il1l1 import ll11llllll11l111Il1l1


__RELOADIUM__ = True

l1ll11l111l11ll1Il1l1 = llll1ll111111lllIl1l1.l11ll1l1ll111111Il1l1(__name__)


@dataclass
class lll1l11111l11111Il1l1:
    l1llll11lllllll1Il1l1: "ll11llllll11l111Il1l1"
    ll11l1l1111l1111Il1l1: l1ll1lllll111l1lIl1l1

    l1lll1ll1lll11llIl1l1: ClassVar[str] = NotImplemented
    ll11lll111ll1l11Il1l1: bool = field(init=False, default=False)

    ll111l11l111lll1Il1l1: ll1l11ll1ll1llllIl1l1 = field(init=False)

    llllll1l11llll11Il1l1: bool = field(init=False, default=False)

    ll1l1ll1111l1111Il1l1 = False

    def __post_init__(ll111ll111ll1lllIl1l1) -> None:
        ll111ll111ll1lllIl1l1.ll111l11l111lll1Il1l1 = llll1ll111111lllIl1l1.l11ll1l1ll111111Il1l1(ll111ll111ll1lllIl1l1.l1lll1ll1lll11llIl1l1)
        ll111ll111ll1lllIl1l1.ll111l11l111lll1Il1l1.llll1lll1ll1ll11Il1l1('Creating extension')
        ll111ll111ll1lllIl1l1.l1llll11lllllll1Il1l1.l1l1l1l1l111111lIl1l1.l1ll1l1l1111ll11Il1l1.ll1ll1l1ll11l1llIl1l1(ll111ll111ll1lllIl1l1.l111l11ll1llll11Il1l1())
        ll111ll111ll1lllIl1l1.llllll1l11llll11Il1l1 = isinstance(ll111ll111ll1lllIl1l1.ll11l1l1111l1111Il1l1, l1l111l11l1lll11Il1l1)

    def l111l11ll1llll11Il1l1(ll111ll111ll1lllIl1l1) -> List[Type[lll1ll1ll111llllIl1l1]]:
        l1l1l11l111111l1Il1l1 = []
        l11111l1ll1ll111Il1l1 = ll111ll111ll1lllIl1l1.ll11l1l11l1l1111Il1l1()
        for ll1ll1ll11ll11l1Il1l1 in l11111l1ll1ll111Il1l1:
            ll1ll1ll11ll11l1Il1l1.ll1111l1l11ll11lIl1l1 = ll111ll111ll1lllIl1l1.l1lll1ll1lll11llIl1l1

        l1l1l11l111111l1Il1l1.extend(l11111l1ll1ll111Il1l1)
        return l1l1l11l111111l1Il1l1

    def ll111lllllll111lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        ll111ll111ll1lllIl1l1.ll11lll111ll1l11Il1l1 = True

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        pass

    @classmethod
    def l1ll11llll11111lIl1l1(l1lll1111111ll11Il1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> bool:
        if ( not hasattr(ll1ll111ll1l11llIl1l1, '__name__')):
            return False

        l1l1l11l111111l1Il1l1 = ll1ll111ll1l11llIl1l1.__name__.split('.')[0].lower() == l1lll1111111ll11Il1l1.l1lll1ll1lll11llIl1l1.lower()
        return l1l1l11l111111l1Il1l1

    def l1llllll1l1lll1lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        l1ll11l111l11ll1Il1l1.llll1lll1ll1ll11Il1l1(''.join(['Disabling extension ', '{:{}}'.format(ll111ll111ll1lllIl1l1.l1lll1ll1lll11llIl1l1, '')]))

    @contextmanager
    def llll11l1111l1ll1Il1l1(ll111ll111ll1lllIl1l1) -> Generator[None, None, None]:
        yield 

    def l11l1l111l111111Il1l1(ll111ll111ll1lllIl1l1) -> None:
        pass

    def ll1l1l1l11l111l1Il1l1(ll111ll111ll1lllIl1l1, l1111l1ll111l111Il1l1: Exception) -> None:
        pass

    def ll1ll111111l1ll1Il1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str, l1lll1111l1lll1lIl1l1: bool) -> Optional[ll11111l1l1111llIl1l1]:
        return None

    async def l111l1ll11llllllIl1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str) -> Optional[l1111l111l1l1l1lIl1l1]:
        return None

    def l111lll1ll11lll1Il1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str) -> Optional[ll11111l1l1111llIl1l1]:
        return None

    async def lllllllll111111lIl1l1(ll111ll111ll1lllIl1l1, lll111ll111ll1l1Il1l1: str) -> Optional[l1111l111l1l1l1lIl1l1]:
        return None

    def ll1111l1l1ll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        pass

    def lll1llll1lll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        pass

    def l1l11l1llll11l11Il1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path, l1l1l111llllll1lIl1l1: List[l1l1l1llll1ll11lIl1l1]) -> None:
        pass

    def __eq__(ll111ll111ll1lllIl1l1, ll1ll1lll1l1111lIl1l1: Any) -> bool:
        return id(ll1ll1lll1l1111lIl1l1) == id(ll111ll111ll1lllIl1l1)

    def ll11l1l11l1l1111Il1l1(ll111ll111ll1lllIl1l1) -> List[Type[lll1ll1ll111llllIl1l1]]:
        return []

    def ll11111l11l111l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType, lll111ll111ll1l1Il1l1: str) -> bool:
        l1l1l11l111111l1Il1l1 = (hasattr(ll1ll111ll1l11llIl1l1, '__name__') and ll1ll111ll1l11llIl1l1.__name__ == lll111ll111ll1l1Il1l1)
        return l1l1l11l111111l1Il1l1


@dataclass(repr=False)
class l11l1l1ll1lllll1Il1l1(ll11111l1l1111llIl1l1):
    ll11l1lll1llll11Il1l1: lll1l11111l11111Il1l1

    def __repr__(ll111ll111ll1lllIl1l1) -> str:
        return 'ExtensionMemento'


@dataclass(repr=False)
class l11l11lllllll111Il1l1(l1111l111l1l1l1lIl1l1):
    ll11l1lll1llll11Il1l1: lll1l11111l11111Il1l1

    def __repr__(ll111ll111ll1lllIl1l1) -> str:
        return 'AsyncExtensionMemento'
