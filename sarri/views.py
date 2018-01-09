import json

import pylla
from pylla.views import View
from pylla.responses import HttpResponse
from pylla.cache import get_from_cache, set_value_in_cache
from pylla.templates import load_template
from pylla.utils import absolute_url

import settings
from sarri.utils import pick_og_image

class MainView(View):
    def get(self, req):
        context = {
            'live_url' : settings.LIVE_URL,
            'og_image_url' :  pick_og_image()
        }
        return HttpResponse(
            load_template('sarri/index.html', context),
        )


class MainResource:
    def on_get(self, req, resp):
        resp.status = pylla.HTTP_200
        resp.content_type = 'text/html'
        context = {
            'live_url' : settings.LIVE_URL,
            'og_image_url' :  pick_og_image()
        }
        resp.body = load_template('sarri/index.html', context)
