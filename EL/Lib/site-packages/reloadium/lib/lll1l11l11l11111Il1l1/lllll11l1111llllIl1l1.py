import sys

from reloadium.corium.l1llll1llll11l1lIl1l1.l11l1l1lll1ll11lIl1l1 import l11111l1111l11l1Il1l1

__RELOADIUM__ = True

l11111l1111l11l1Il1l1()


try:
    import _pytest.assertion.rewrite
except ImportError:
    class lll1ll1lll11l1l1Il1l1:
        pass

    _pytest = lambda :None  # type: ignore
    sys.modules['_pytest'] = _pytest

    _pytest.assertion = lambda :None  # type: ignore
    sys.modules['_pytest.assertion'] = _pytest.assertion

    _pytest.assertion.rewrite = lambda :None  # type: ignore
    _pytest.assertion.rewrite.AssertionRewritingHook = lll1ll1lll11l1l1Il1l1  # type: ignore
    sys.modules['_pytest.assertion.rewrite'] = _pytest.assertion.rewrite
