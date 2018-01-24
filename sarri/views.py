import json

import ukumuku
from ukumuku.views import View
from ukumuku.responses import HttpResponse
from ukumuku.cache import get_from_cache, set_value_in_cache
from ukumuku.templates import template_engine
from ukumuku.utils import absolute_url

import settings
from sarri.utils import pick_og_image

class MainView(View):
    def get(self, req):
        context = {
            'live_url' : settings.LIVE_URL,
            'og_image_url' :  pick_og_image()
        }
        return HttpResponse(
            template_engine.render_template('sarri/index.html', context),
        )


class MainResource:
    def on_get(self, req, resp):
        resp.status = ukumuku.HTTP_200
        resp.content_type = 'text/html'
        context = {
            'live_url' : settings.LIVE_URL,
            'og_image_url' :  pick_og_image()
        }
        resp.body = template_engine.render_template('sarri/index.html', context)
