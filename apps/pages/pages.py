from pages import models


def get_page_urls():
    """Получает все известные публичные ссылки для sitemap.xml в рамках текущего приложения"""
    pages = models.FlatPage.objects.published()
    for page in pages:
        yield page.get_absolute_url()
