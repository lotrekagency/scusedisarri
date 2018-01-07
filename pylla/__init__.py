import falcon

from .status_codes import *

class App():

    app = None

    def __init__(self):
        pass

    def start(self):
        self.app = falcon.API()
        return self.app