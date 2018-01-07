import falcon
import os
import logging
import json
import random

from wsgi_static_middleware import StaticMiddleware
from falcon_sslify import FalconSSLify

import pylla
from pylla.views import View
from pylla.responses import HttpResponse
from pylla.cache import get_from_cache, set_value_in_cache
from pylla.templates import load_template

BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'public')]
LIVE_URL = 'https://www.scusedisarri.it'

log = logging.getLogger('SarriLogger')


def pick_quote(searched_quote=None):
    data = get_from_cache('quotes')
    if not data:
        f = open('resources/quotes.json')
        quotes_json = f.read() 
        data = json.loads(quotes_json)
        set_value_in_cache('quotes', quotes_json)
        f.close()
    else:
        data = json.loads(data)
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
    else:
        data = json.loads(data)
    number_of_images = len(data["og_images"])
    og_image_index = random.randint(0,number_of_images-1)
    return data["og_images"][og_image_index]["url"]


class MainResource(View):
    def get(self, req):
        context = {
            'live_url' : LIVE_URL,
            'og_image_url' :  pick_og_image()
        }
        return HttpResponse(
            load_template('index.html', context),
        )


class QuoteResource(View):
    def get(self, req, quote=None):
        picked_quote = pick_quote(quote)
        if picked_quote == None:
            return HttpResponse('', pylla.HTTP_301, headers={'Location' : '/dice'})
        else:
            context = picked_quote
            context.update({
                'live_url' : LIVE_URL,
                'og_image_url' :  pick_og_image()
            })
            return HttpResponse(
                load_template('quote.html', context),
            )


app = pylla.App().start()
    #app = falcon.API(middleware=[sslify])
app.add_route('/', MainResource())
app.add_route('/dice', QuoteResource())
app.add_route('/dice/{quote}', QuoteResource())
app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)
