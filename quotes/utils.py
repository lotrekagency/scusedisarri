import json
import random

from ukumuku.cache import get_from_cache, set_value_in_cache


def pick_quote(searched_quote=None):
    data = get_from_cache('quotes')
    if not data:
        f = open('resources/quotes.json')
        quotes_json = f.read() 
        data = json.loads(quotes_json)
        set_value_in_cache('quotes', quotes_json)
        f.close()
    else:
        data = json.loads(data)
    if searched_quote:
        for quote in data["quotes"]:
            if quote['quote_url_share'] == searched_quote:
                return (quote)
        return None
    else:
        number_of_quotes = len(data["quotes"])
        quote_index = random.randint(0, number_of_quotes-1)
        quote = data["quotes"][quote_index]
    return (quote)
