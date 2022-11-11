import sys

import collections
from django.conf import settings


def collect_sitemap_urls():
    urls = []
    for app_label in settings.INSTALLED_APPS:
        mod_name = '.'.join((app_label, 'pages'))
        try:
            __import__(mod_name, {}, {}, [], 0)
            mod = sys.modules[mod_name]
            names = dir(mod)
            if 'get_page_urls' in names:
                global_func = mod.get_page_urls
                for lang in settings.LANGUAGE_CODES_PUBLIC:
                    prefix = '' if lang == settings.LANGUAGE_CODE else f'/{lang}'
                    result = global_func()
                    if result and isinstance(result, collections.Iterable):
                        urls.extend([f'{prefix}{x}' for x in result])
        except ImportError:
            pass

    return urls
