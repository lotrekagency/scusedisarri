from pylla.views import View
from pylla.responses import HttpResponse
from pylla.cache import get_from_cache, set_value_in_cache
from pylla.templates import load_template

from sarri.utils import pick_og_image
import settings

from .utils import pick_quote


class QuoteView(View):
    def get(self, req, quote=None):
        picked_quote = pick_quote(quote)
        if picked_quote == None:
            return HttpResponse('', pylla.HTTP_301, headers={'Location' : '/dice'})
        else:
            context = picked_quote
            context.update({
                'live_url' : settings.LIVE_URL,
                'og_image_url' :  pick_og_image()
            })
            return HttpResponse(
                load_template('quote.html', context),
            )