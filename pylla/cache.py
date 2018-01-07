try:
    import bmemcached
    memcached = bmemcached.Client(
        os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','), 
        os.environ.get('MEMCACHEDCLOUD_USERNAME'), 
        os.environ.get('MEMCACHEDCLOUD_PASSWORD')
    )
except:
    from pymemcache.client.base import Client
    memcached = Client(('127.0.0.1', 11211))


def get_from_cache(key):
    value = memcached.get('SARRI-' + key)
    return value


def set_value_in_cache(key, value):
    value = memcached.set('SARRI-' + key, value.encode('UTF-8'))
    return value