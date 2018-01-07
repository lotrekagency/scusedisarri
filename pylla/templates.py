import pystache

from .cache import get_from_cache, set_value_in_cache


def load_template(filename, context={}):
    content = get_from_cache(filename)
    if not content:
        f = open('public/templates/' + filename)
        content = f.read()
        set_value_in_cache(filename, content)
        f.close()
    return pystache.render(content, context)
