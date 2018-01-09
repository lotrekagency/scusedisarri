import os

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

SSL = False
