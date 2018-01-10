import falcon
import importlib
import settings


class App(falcon.API):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        for static_dir in settings.STATIC_DIRS:
            self.add_static_route(settings.STATIC_URL, static_dir)

    def add_routes(self, urls_module_path):
        urls_module = importlib.import_module(urls_module_path)
        for url in urls_module.urls:
            self.add_route(url[0], url[1])
