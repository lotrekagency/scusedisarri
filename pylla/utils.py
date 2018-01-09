
from falcon import uri


def absolute_url(req):
    print (uri.parse_host(req.url))