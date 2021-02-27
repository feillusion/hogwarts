from mitmproxy import ctx
from mitmproxy import http

#利用mitmproxy实现maplocal
class MaplocalTest:
    def __init__(self):
        self.num = 0
    def request(self, flow: http.HTTPFlow) -> None:
        if "/v5/stock/batch/quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
          with open("mock.json", 'r', encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

addons = [
    MaplocalTest()
]