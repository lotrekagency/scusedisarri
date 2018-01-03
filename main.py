import falcon

def load_template(filename, context={}):
    f = open('public/templates/' + filename)
    return f.read()

class MainResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = load_template('index.html')

class QuoteResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = load_template('says.html')


api = falcon.API()
api.add_route('/', MainResource())
api.add_route('/dice', QuoteResource())