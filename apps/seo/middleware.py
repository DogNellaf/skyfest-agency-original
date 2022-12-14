from django.conf import settings
from django.http import HttpResponseGone, HttpResponsePermanentRedirect, \
    HttpResponseRedirect, HttpResponseNotModified
from django.http.response import HttpResponseRedirectBase
from django.utils.deprecation import MiddlewareMixin

from seo.choices import RedirectCodeChoices
from seo.router import router
from seo.models import SEOPage


class SEOMiddleware(MiddlewareMixin):
    """Middleware adds some template context variables"""
    @staticmethod
    def process_request(request):
        path = request.get_full_path()
        if not path.endswith('/') and settings.APPEND_SLASH:
            path += '/'
        redirect = router.get_path(path)
        if redirect is not None:
            status_code = int(redirect.status_code)
            if redirect.new_path == '' or status_code == RedirectCodeChoices.C410.value:
                return HttpResponseGone()
            elif status_code == RedirectCodeChoices.C301.value:
                return HttpResponsePermanentRedirect(redirect.new_path)
            elif status_code == RedirectCodeChoices.C302.value:
                return HttpResponseRedirect(redirect.new_path)
            elif status_code == RedirectCodeChoices.C304.value:
                return HttpResponseNotModified(redirect.new_path)
            response = HttpResponseRedirectBase(redirect.new_path)
            response.status_code = status_code
            return response

        try:
            full_path_parts = request.get_full_path().split('/')
            full_path_parts[1] = ''
            full_path = '/'.join(full_path_parts[1:])
            seo_page = SEOPage.objects.published().get(url__iexact=full_path)
            seo_page.apply_seo_params(request)

        except (SEOPage.DoesNotExist, SEOPage.MultipleObjectsReturned):
            pass

        return None
