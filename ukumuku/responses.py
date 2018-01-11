from falcon.response import Response
from .status_codes import *


class HttpResponse():

    body = ''
    status = HTTP_200
    content_type = 'text/html'
    headers = {}

    def __init__(self, body, status=HTTP_200, content_type='text/html', headers={}):
        self.body = body
        self.status = status
        self.content_type = content_type

    def to_response(self, resp):
        resp.body = self.body
        resp.status = self.status
        resp.content_type = self.content_type
        #resp.headers = self.headers
        

class JSONResponse():
    pass

class TemplateResponse():
    pass