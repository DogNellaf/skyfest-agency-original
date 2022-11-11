from homepage import models


def get_page_urls():
    """Получает все известные публичные ссылки для sitemap.xml в рамках текущего приложения"""
    yield models.HomePage.get_absolute_url()
