import falcon
import os
import pystache
import logging
import json
import random
from wsgi_static_middleware import StaticMiddleware


BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'public')]

log = logging.getLogger('SarriLogger')

def load_template(filename, context={}):
    f = open('public/templates/' + filename)
    content = f.read()
    return pystache.render(content, context)

def pick_quote(searched_quote=None):
    data = json.load(open('resources/quotes.json'))
    if searched_quote:
        for quote in data["quotes"]:
            if quote['quote_url_share'] == searched_quote:
                return (quote)
        return None
    else:
        number_of_quotes = len(data["quotes"])
        quote_index = random.randint(0, number_of_quotes-1)
        quote = data["quotes"][quote_index]
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
    def on_get(self, req, resp, quote=None):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        picked_quote = pick_quote(quote)

        if picked_quote == None:
            resp.status = falcon.HTTP_301
            resp.set_header('Location', '/dice')
        else:
            context = picked_quote
            resp.body = load_template('quote.html', context)


app = falcon.API()

app.add_route('/', MainResource())
app.add_route('/dice', QuoteResource())
app.add_route('/dice/{quote}', QuoteResource())
app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)
