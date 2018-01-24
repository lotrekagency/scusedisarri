from ukumuku.responses import HttpResponse
from falcon.response import Response

resp = Response()

def benchmark():
    for i in range(0,100):
        HttpResponse(body='a').to_response(resp)

import profile
profile.run("benchmark()")