from blog import models


def get_page_urls():
    """Получает все известные публичные ссылки для sitemap.xml в рамках текущего приложения"""
    yield models.BlogPage.get_absolute_url()

    pages = models.Article.objects.published().actual()
    for page in pages:
        yield page.get_absolute_url()
