import os

DEBUG = True

BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
STATIC_DIRS = [os.path.join(BASE_DIR, 'public')]
STATIC_URL = '/static'
LIVE_URL = 'https://www.scusedisarri.it'

MEMCACHED = {
    'servers':(
        ('127.0.0.1:11211')
    ),
    'settings' : {
        'username' : None,
        'password' : None
    }
}

SSL_REDIRECT = False
BASE_LOOKUP_DIR = './'

try:
    from .local import *
except ImportError:
    pass

try:
    from .deploy import *
    print ("\n\nSTART DEPLOYED APP!\n\n")
except ImportError:
    pass