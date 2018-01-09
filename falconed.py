import falcon
import os
import logging
import json
import random
import settings

from sarri.views import MainResource
from quotes.views import QuoteResource


app = falcon.API()

app.add_route('/', MainResource())
app.add_route('/dice', QuoteResource())
app.add_route('/dice/{quote}', QuoteResource())
for static_dir in settings.STATIC_DIRS:
    app.add_static_route(settings.STATIC_URL, static_dir)