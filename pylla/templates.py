import os

from .cache import get_from_cache, set_value_in_cache

from mako.template import Template
from mako.lookup import TemplateLookup


tempalte_directories = []
for directory in os.listdir('./'):
    sub_directory = os.path.join(directory, 'templates')
    if directory == 'templates':
        tempalte_directories.append(directory)
    elif os.path.isdir(sub_directory):
        tempalte_directories.append(sub_directory)
print (tempalte_directories)
template_lookup = TemplateLookup(directories=tempalte_directories)


def load_template(template_name, context={}):
    mytemplate = template_lookup.get_template(template_name)
    return mytemplate.render(**context)
