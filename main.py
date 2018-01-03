import falcon
import os
import pystache
import logging
import json
import random
from wsgi_static_middleware import StaticMiddleware


BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'static')]

log = logging.getLogger('SarriLogger')

def load_template(filename, context={}):
    f = open('public/templates/' + filename)
    content = f.read()
    return pystache.render(content, context)

def pick_quote():
    data = json.load(open('resources/quotes.json'))
    number_of_quotes = len(data["quotes"])
    quote_index = random.randint(0,number_of_quotes-1)
    quote = data["quotes"][quote_index]
    log.error(quote)
    return (quote)

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
        context = pick_quote()

        resp.body = load_template('quote.html', context)


app = falcon.API()

app.add_route('/', MainResource())
app.add_route('/dice', QuoteResource())
app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)
