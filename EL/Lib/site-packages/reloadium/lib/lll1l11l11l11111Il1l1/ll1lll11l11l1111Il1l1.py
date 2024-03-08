from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, List

from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1
from reloadium.corium.l11111l1ll1ll111Il1l1 import l1l1l1llll1ll11lIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1 import lll11ll111ll1l11Il1l1
from dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l11111l1lll1ll11Il1l1(lll1l11111l11111Il1l1):
    l1lll1ll1lll11llIl1l1 = 'PyGame'

    ll1l1ll1111l1111Il1l1 = True

    l11lll11l111ll11Il1l1: bool = field(init=False, default=False)

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, l1lll1l11111lll1Il1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(l1lll1l11111lll1Il1l1, 'pygame.base')):
            ll111ll111ll1lllIl1l1.ll111l1l1lll1lllIl1l1()

    def ll111l1l1lll1lllIl1l1(ll111ll111ll1lllIl1l1) -> None:
        import pygame.display

        l1111111111l1l1lIl1l1 = pygame.display.update

        def l11ll1lll1l111l1Il1l1(*l11111l1111llll1Il1l1: Any, **ll1l1lll11l1l11lIl1l1: Any) -> None:
            if (ll111ll111ll1lllIl1l1.l11lll11l111ll11Il1l1):
                lll11ll111ll1l11Il1l1.ll11lll11l1lllllIl1l1(0.1)
                return None
            else:
                return l1111111111l1l1lIl1l1(*l11111l1111llll1Il1l1, **ll1l1lll11l1l11lIl1l1)

        pygame.display.update = l11ll1lll1l111l1Il1l1

    def lll1llll1lll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        ll111ll111ll1lllIl1l1.l11lll11l111ll11Il1l1 = True

    def l1l11l1llll11l11Il1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path, l1l1l111llllll1lIl1l1: List[l1l1l1llll1ll11lIl1l1]) -> None:
        ll111ll111ll1lllIl1l1.l11lll11l111ll11Il1l1 = False

    def ll1l1l1l11l111l1Il1l1(ll111ll111ll1lllIl1l1, l1111l1ll111l111Il1l1: Exception) -> None:
        ll111ll111ll1lllIl1l1.l11lll11l111ll11Il1l1 = False
