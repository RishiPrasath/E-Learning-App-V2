import dataclasses
import types
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1
from reloadium.fast.lll1l11l11l11111Il1l1.lll111lll1lll1l1Il1l1 import ll111111lll1111lIl1l1

from dataclasses import dataclass

__RELOADIUM__ = True

import types


@dataclass(repr=False, frozen=False)
class ll1l1llll11l111lIl1l1(lll1l11111l11111Il1l1):
    l1lll1ll1lll11llIl1l1 = 'Pytest'

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'pytest')):
            ll111ll111ll1lllIl1l1.ll1ll1111l1l11llIl1l1(ll1ll111ll1l11llIl1l1)

    def ll1ll1111l1l11llIl1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        import _pytest.assertion.rewrite
        _pytest.assertion.rewrite.AssertionRewritingHook = ll111111lll1111lIl1l1  # type: ignore

