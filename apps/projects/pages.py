from projects import models


def get_page_urls():
    """Получает все известные публичные ссылки для sitemap.xml в рамках текущего приложения"""
    yield models.ProjectsPage.get_absolute_url()

    pages = models.Project.objects.published()
    for page in pages:
        yield page.get_absolute_url()
