import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type, Union, cast

from reloadium.corium.l111111l11ll1ll1Il1l1 import l1lllll1111lll11Il1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1
from reloadium.lib import extensions_raw
from reloadium.corium.l11l11l11111llllIl1l1 import lllllllllll11l1lIl1l1
from dataclasses import dataclass

if (TYPE_CHECKING):
    ...


__RELOADIUM__ = True


@dataclass
class ll1l1l1ll111111lIl1l1(lll1l11111l11111Il1l1):
    l1lll1ll1lll11llIl1l1 = 'Multiprocessing'

    ll1l1ll1111l1111Il1l1 = True

    def __post_init__(ll111ll111ll1lllIl1l1) -> None:
        super().__post_init__()

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'multiprocessing.popen_spawn_posix')):
            ll111ll111ll1lllIl1l1.l11l1l1l1l11ll11Il1l1(ll1ll111ll1l11llIl1l1)

        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'multiprocessing.popen_spawn_win32')):
            ll111ll111ll1lllIl1l1.lll11ll11l1l1111Il1l1(ll1ll111ll1l11llIl1l1)

    def l11l1l1l1l11ll11Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_posix
        multiprocessing.popen_spawn_posix.Popen._launch = extensions_raw.multiprocessing.posix_popen_launch  # type: ignore

    def lll11ll11l1l1111Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_win32
        multiprocessing.popen_spawn_win32.Popen.__init__ = extensions_raw.multiprocessing.wind32_popen_launch  # type: ignore
