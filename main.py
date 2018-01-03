import falcon
import pystache


def load_template(filename, context={}):
    f = open('public/templates/' + filename)
    content = f.read()
    return pystache.render(content, context)

class MainResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        context = {
            'title' : 'SARRY'
        }
        resp.body = load_template('index.html', context)

class QuoteResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = load_template('says.html')


api = falcon.API()
api.add_route('/', MainResource())
api.add_route('/dice', QuoteResource())