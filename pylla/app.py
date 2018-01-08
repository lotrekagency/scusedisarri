import falcon
import importlib



class App(falcon.API):
    
    def add_routes(self, urls_module_path):
        urls_module = importlib.import_module(urls_module_path)
        for url in urls_module.urls:
            self.add_route(url[0], url[1])

