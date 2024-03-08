from reloadium.corium.vendored import logging
from pathlib import Path
from threading import Thread
import time
from typing import TYPE_CHECKING, List, Optional

from reloadium.corium import l1llll1llll11l1lIl1l1
from reloadium.corium.l1llll1llll11l1lIl1l1.l11lll111l11ll1lIl1l1 import ll11111lll11ll1lIl1l1
from reloadium.lib.lll1l11l11l11111Il1l1.ll11l1lll1llll11Il1l1 import lll1l11111l11111Il1l1
from reloadium.corium.l11l11l11111llllIl1l1 import lllllllllll11l1lIl1l1
from reloadium.corium.llll1ll111111lllIl1l1 import ll1l11ll1ll1llllIl1l1
from reloadium.corium.l11111l1ll1ll111Il1l1 import l1l1l1llll1ll11lIl1l1
from reloadium.corium.l1l1111llllll1l1Il1l1 import l1l1111llllll1l1Il1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.vendored.websocket_server import WebsocketServer


__RELOADIUM__ = True

__all__ = ['l1l1111l11l11ll1Il1l1']



lll111l1l1l11lllIl1l1 = '\n<!--{info}-->\n<script type="text/javascript">\n   // <![CDATA[  <-- For SVG support\n     function refreshCSS() {\n        var sheets = [].slice.call(document.getElementsByTagName("link"));\n        var head = document.getElementsByTagName("head")[0];\n        for (var i = 0; i < sheets.length; ++i) {\n           var elem = sheets[i];\n           var parent = elem.parentElement || head;\n           parent.removeChild(elem);\n           var rel = elem.rel;\n           if (elem.href && typeof rel != "string" || rel.length === 0 || rel.toLowerCase() === "stylesheet") {\n              var url = elem.href.replace(/(&|\\?)_cacheOverride=\\d+/, \'\');\n              elem.href = url + (url.indexOf(\'?\') >= 0 ? \'&\' : \'?\') + \'_cacheOverride=\' + (new Date().valueOf());\n           }\n           parent.appendChild(elem);\n        }\n     }\n     let protocol = window.location.protocol === \'http:\' ? \'ws://\' : \'wss://\';\n     let address = protocol + "{address}:{port}";\n     let socket = undefined;\n     let lost_connection = false;\n\n     function connect() {\n        socket = new WebSocket(address);\n         socket.onmessage = function (msg) {\n            if (msg.data === \'reload\') window.location.href = window.location.href;\n            else if (msg.data === \'refreshcss\') refreshCSS();\n         };\n     }\n\n     function checkConnection() {\n        if ( socket.readyState === socket.CLOSED ) {\n            lost_connection = true;\n            connect();\n        }\n     }\n\n     connect();\n     setInterval(checkConnection, 500)\n\n   // ]]>\n</script>\n'














































@dataclass
class l1l1111l11l11ll1Il1l1:
    l11l1l11111l1111Il1l1: str
    l11lll1llll1l1llIl1l1: int
    l1ll11l111l11ll1Il1l1: ll1l11ll1ll1llllIl1l1

    lll111l11ll1111lIl1l1: Optional["WebsocketServer"] = field(init=False, default=None)
    lll1l11lll1lll1lIl1l1: str = field(init=False, default='')

    llll1lll1ll1ll11Il1l1 = 'Reloadium page reloader'

    def l1l11llllll1lll1Il1l1(ll111ll111ll1lllIl1l1) -> None:
        from reloadium.vendored.websocket_server import WebsocketServer

        ll111ll111ll1lllIl1l1.l1ll11l111l11ll1Il1l1.llll1lll1ll1ll11Il1l1(''.join(['Starting reload websocket server on port ', '{:{}}'.format(ll111ll111ll1lllIl1l1.l11lll1llll1l1llIl1l1, '')]))

        ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1 = WebsocketServer(host=ll111ll111ll1lllIl1l1.l11l1l11111l1111Il1l1, port=ll111ll111ll1lllIl1l1.l11lll1llll1l1llIl1l1)
        ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1.run_forever(threaded=True)

        ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1 = lll111l1l1l11lllIl1l1

        ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1 = ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1.replace('{info}', str(ll111ll111ll1lllIl1l1.llll1lll1ll1ll11Il1l1))
        ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1 = ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1.replace('{port}', str(ll111ll111ll1lllIl1l1.l11lll1llll1l1llIl1l1))
        ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1 = ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1.replace('{address}', ll111ll111ll1lllIl1l1.l11l1l11111l1111Il1l1)

    def l1ll11l11l1l1lllIl1l1(ll111ll111ll1lllIl1l1, l1ll1lll111ll1llIl1l1: str) -> str:
        ll1lll1l111111llIl1l1 = l1ll1lll111ll1llIl1l1.find('<head>')
        if (ll1lll1l111111llIl1l1 ==  - 1):
            ll1lll1l111111llIl1l1 = 0
        l1l1l11l111111l1Il1l1 = ((l1ll1lll111ll1llIl1l1[:ll1lll1l111111llIl1l1] + ll111ll111ll1lllIl1l1.lll1l11lll1lll1lIl1l1) + l1ll1lll111ll1llIl1l1[ll1lll1l111111llIl1l1:])
        return l1l1l11l111111l1Il1l1

    def l1l1lllll11l1lllIl1l1(ll111ll111ll1lllIl1l1) -> None:
        try:
            ll111ll111ll1lllIl1l1.l1l11llllll1lll1Il1l1()
        except Exception as l11l11l11111l1llIl1l1:
            ll111ll111ll1lllIl1l1.l1ll11l111l11ll1Il1l1.l1111llll1111l1lIl1l1('Could not start page reload server', lllll11llll11l11Il1l1=True)

    def lll1l1111111l11lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        if ( not ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l1ll11l111l11ll1Il1l1.llll1lll1ll1ll11Il1l1('Reloading page')
        ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1.send_message_to_all('reload')
        l1l1111llllll1l1Il1l1.l11111llllllll1lIl1l1()

    def lll1ll1lll11l111Il1l1(ll111ll111ll1lllIl1l1) -> None:
        if ( not ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1):
            return 

        ll111ll111ll1lllIl1l1.l1ll11l111l11ll1Il1l1.llll1lll1ll1ll11Il1l1('Stopping reload server')
        ll111ll111ll1lllIl1l1.lll111l11ll1111lIl1l1.shutdown()

    def lllll1l111l1ll1lIl1l1(ll111ll111ll1lllIl1l1, ll11l1l111111lllIl1l1: float) -> None:
        def l1l1ll111l1ll11lIl1l1() -> None:
            time.sleep(ll11l1l111111lllIl1l1)
            ll111ll111ll1lllIl1l1.lll1l1111111l11lIl1l1()

        ll11111lll11ll1lIl1l1(ll11l11l1l11ll11Il1l1=l1l1ll111l1ll11lIl1l1, lll111ll111ll1l1Il1l1='page-reloader').start()


@dataclass
class lllll111l1l1l1llIl1l1(lll1l11111l11111Il1l1):
    lll111l1l1l11lllIl1l1: Optional[l1l1111l11l11ll1Il1l1] = field(init=False, default=None)

    ll1111lll1111ll1Il1l1 = '127.0.0.1'
    l1ll1111llllll11Il1l1 = 4512

    def l11l1l111l111111Il1l1(ll111ll111ll1lllIl1l1) -> None:
        lllllllllll11l1lIl1l1.l1l1l1l1l111111lIl1l1.l11111l111l1l11lIl1l1.l11lll1ll1l111l1Il1l1('html')

    def l1l11l1llll11l11Il1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path, l1l1l111llllll1lIl1l1: List[l1l1l1llll1ll11lIl1l1]) -> None:
        if ( not ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
            return 

        from reloadium.corium.l11l111l1lll1l11Il1l1.ll11l11ll1l1l111Il1l1 import l1llll11l1l111l1Il1l1

        if ( not any((isinstance(ll111111l1l1l11lIl1l1, l1llll11l1l111l1Il1l1) for ll111111l1l1l11lIl1l1 in l1l1l111llllll1lIl1l1))):
            if (ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
                ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.lll1l1111111l11lIl1l1()

    def ll1111l1l1ll11llIl1l1(ll111ll111ll1lllIl1l1, ll11l11111l1ll11Il1l1: Path) -> None:
        if ( not ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
            return 
        ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.lll1l1111111l11lIl1l1()

    def l11ll1l1111l1ll1Il1l1(ll111ll111ll1lllIl1l1, l11lll1llll1l1llIl1l1: int) -> l1l1111l11l11ll1Il1l1:
        while True:
            llll1l1lll1lll1lIl1l1 = (l11lll1llll1l1llIl1l1 + ll111ll111ll1lllIl1l1.l1ll1111llllll11Il1l1)
            try:
                l1l1l11l111111l1Il1l1 = l1l1111l11l11ll1Il1l1(l11l1l11111l1111Il1l1=ll111ll111ll1lllIl1l1.ll1111lll1111ll1Il1l1, l11lll1llll1l1llIl1l1=llll1l1lll1lll1lIl1l1, l1ll11l111l11ll1Il1l1=ll111ll111ll1lllIl1l1.ll111l11l111lll1Il1l1)
                l1l1l11l111111l1Il1l1.l1l1lllll11l1lllIl1l1()
                ll111ll111ll1lllIl1l1.llllll1ll1l111llIl1l1()
                break
            except OSError:
                ll111ll111ll1lllIl1l1.ll111l11l111lll1Il1l1.llll1lll1ll1ll11Il1l1(''.join(["Couldn't create page reloader on ", '{:{}}'.format(llll1l1lll1lll1lIl1l1, ''), ' port']))
                ll111ll111ll1lllIl1l1.l1ll1111llllll11Il1l1 += 1

        return l1l1l11l111111l1Il1l1

    def llllll1ll1l111llIl1l1(ll111ll111ll1lllIl1l1) -> None:
        ll111ll111ll1lllIl1l1.ll111l11l111lll1Il1l1.llll1lll1ll1ll11Il1l1('Injecting page reloader')

    def l1llllll1l1lll1lIl1l1(ll111ll111ll1lllIl1l1) -> None:
        super().l1llllll1l1lll1lIl1l1()

        if (ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1):
            ll111ll111ll1lllIl1l1.lll111l1l1l11lllIl1l1.lll1ll1lll11l111Il1l1()
