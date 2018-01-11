import json
import random

from ukumuku.cache import get_from_cache, set_value_in_cache


def pick_og_image():
    data = get_from_cache('quotes')
    if not data:
        f = open('resources/quotes.json')
        quotes_json = f.read() 
        data = json.loads(quotes_json)
        set_value_in_cache('quotes', quotes_json)
        f.close()
    else:
        data = json.loads(data)
    number_of_images = len(data["og_images"])
    og_image_index = random.randint(0,number_of_images-1)
    return data["og_images"][og_image_index]["url"]


