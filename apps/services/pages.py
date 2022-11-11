from services import models


def get_page_urls():
    """Получает все известные публичные ссылки для sitemap.xml в рамках текущего приложения"""
    yield models.ServicesPage.get_absolute_url()

    pages = models.Service.objects.published()
    for page in pages:
        yield page.get_absolute_url()
