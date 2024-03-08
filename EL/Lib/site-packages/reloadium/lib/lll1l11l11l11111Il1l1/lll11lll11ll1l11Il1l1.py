from dataclasses import dataclass, field
from types import CodeType, ModuleType
from typing import TYPE_CHECKING, Any, Callable, Optional
import inspect

from reloadium.lib.lll1l11l11l11111Il1l1.ll1l1ll11lll11l1Il1l1 import lllll111l1l1l1llIl1l1

if (TYPE_CHECKING):
    pass


__RELOADIUM__ = True


@dataclass
class ll1ll11lll11ll11Il1l1(lllll111l1l1l1llIl1l1):
    l1lll1ll1lll11llIl1l1 = 'Numba'

    ll1l1ll1111l1111Il1l1 = True

    def __post_init__(ll111ll111ll1lllIl1l1) -> None:
        super().__post_init__()

    def l111ll1ll1l1l1l1Il1l1(ll111ll111ll1lllIl1l1, ll1ll111ll1l11llIl1l1: ModuleType) -> None:
        if (ll111ll111ll1lllIl1l1.ll11111l11l111l1Il1l1(ll1ll111ll1l11llIl1l1, 'numba.core.bytecode')):
            ll111ll111ll1lllIl1l1.l1ll11l11111l1llIl1l1()

    def l1ll11l11111l1llIl1l1(ll111ll111ll1lllIl1l1) -> None:
        import numba.core.bytecode

        def llllll1l1ll111llIl1l1(l1ll11l11l11llllIl1l1) -> CodeType:  # type: ignore
            import ast
            l1l1l11l111111l1Il1l1 = getattr(l1ll11l11l11llllIl1l1, '__code__', getattr(l1ll11l11l11llllIl1l1, 'func_code', None))  # type: ignore

            if ('__rw_mode__' in l1l1l11l111111l1Il1l1.co_consts):  # type: ignore
                ll11l1l11ll11l1lIl1l1 = ast.parse(inspect.getsource(l1ll11l11l11llllIl1l1))
                l11l1lll1l111111Il1l1 = ll11l1l11ll11l1lIl1l1.body[0]
                l11l1lll1l111111Il1l1.decorator_list = []  # type: ignore

                l111l1ll111llll1Il1l1 = compile(ll11l1l11ll11l1lIl1l1, filename=l1l1l11l111111l1Il1l1.co_filename, mode='exec')  # type: ignore
                l1l1l11l111111l1Il1l1 = l111l1ll111llll1Il1l1.co_consts[0]

            return l1l1l11l111111l1Il1l1  # type: ignore

        numba.core.bytecode.get_code_object.__code__ = llllll1l1ll111llIl1l1.__code__
