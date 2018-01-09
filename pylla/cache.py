import settings
import bmemcached

try:
    memcached = bmemcached.Client(
        settings.MEMCACHED['servers'],
        **settings.MEMCACHED['settings']
    )
except Exception as ex:
    print (ex)


def get_from_cache(key):
    value = memcached.get('SARRI-' + key)
    return value


def set_value_in_cache(key, value):
    value = memcached.set('SARRI-' + key, value.encode('UTF-8'))
    return value