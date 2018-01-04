import falcon
import os
import pystache
import logging
import json
import random

from wsgi_static_middleware import StaticMiddleware
from falcon_sslify import FalconSSLify


try:
    import bmemcached
    memcached = bmemcached.Client(
        os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','), 
        os.environ.get('MEMCACHEDCLOUD_USERNAME'), 
        os.environ.get('MEMCACHEDCLOUD_PASSWORD')
    )
except:
    from pymemcache.client.base import Client
    memcached = Client(('localhost', 11211))


BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'public')]
LIVE_URL = 'https://www.scusedisarri.it'

log = logging.getLogger('SarriLogger')


def get_from_cache(key):
    value = memcached.get('SARRI-' + key)
    return value


def set_value_in_cache(key, value):
    value = memcached.set('SARRI-', value.encode('UTF-8'))
    return value


def load_template(filename, context={}):
    content = get_from_cache(filename)
    if not content:
        f = open('public/templates/' + filename)
        content = f.read()
        set_value_in_cache(filename, content)
        f.close()
    return pystache.render(content, context)


def pick_quote(searched_quote=None):
    data = get_from_cache('quotes')
    if not data:
        f = open('resources/quotes.json')
        quotes_json = f.read() 
        data = json.loads(quotes_json)
        set_value_in_cache('quotes', quotes_json)
        f.close()
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


def pick_og_image():
    data = get_from_cache('quotes')
    if not data:
        f = open('resources/quotes.json')
        quotes_json = f.read() 
        data = json.loads(quotes_json)
        set_value_in_cache('quotes', quotes_json)
        f.close()
    number_of_images = len(data["og_images"])
    og_image_index = random.randint(0,number_of_images-1)
    return data["og_images"][og_image_index]["url"]


class MainResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        context = {
            'live_url' : LIVE_URL,
            'og_image_url' :  pick_og_image()
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
            context.update({
                'live_url' : LIVE_URL,
                'og_image_url' :  pick_og_image()
            })
            resp.body = load_template('quote.html', context)


memcached.flush_all()
sslify = FalconSSLify()
app = falcon.API(middleware=[sslify])

app.add_route('/', MainResource())
app.add_route('/dice', QuoteResource())
app.add_route('/dice/{quote}', QuoteResource())
app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)
