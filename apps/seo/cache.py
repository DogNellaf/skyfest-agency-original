import datetime

from seo.models import Redirect


CACHE_TIMEOUT = datetime.timedelta(seconds=60)


class RedirectsCache(object):
    def __init__(self):
        self.last_modified = None
        self.cache = {}

    def index(self, force=False):
        now = datetime.datetime.now()
        if force \
                or self.last_modified is None \
                or now - self.last_modified > CACHE_TIMEOUT:

            redirects = Redirect.objects.published()
            self.cache = {}

            for redirect in redirects.iterator():
                self.cache[redirect.from_url] = (redirect.to_url, redirect.status_code)
            self.last_modified = now

    def force_index(self):
        return self.index(force=True)

    def get(self, url):
        self.index()
        return self.cache.get(url)

    def all(self):
        self.index()
        return self.cache


redirects_cache = RedirectsCache()
