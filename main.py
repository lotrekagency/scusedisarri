from wsgi_static_middleware import StaticMiddleware
#from falcon_sslify import FalconSSLify

import pylla

from sarri import settings


app = pylla.App()
#app = falcon.API(middleware=[sslify])
app.add_routes('sarri.urls')
app.add_routes('quotes.urls')
#app.add_static_route('static', settings.STATIC_DIRS)
app = StaticMiddleware(app, static_root='static', static_dirs=settings.STATIC_DIRS)
