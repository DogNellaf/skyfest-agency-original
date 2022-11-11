from django.shortcuts import get_object_or_404

from pure_pagination import Paginator, EmptyPage, InvalidPage

from blog import models
from snippets.choices import StatusChoices
from snippets.views import BaseTemplateView, LangViewMixin


ARTICLES_PER_PAGE = 5


class ArticleView(LangViewMixin, BaseTemplateView):
    """Страница статьи"""

    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ArticleView, self).get_context_data(**kwargs)
        list_page = models.BlogPage.get_solo()
        article = get_object_or_404(
            models.Article.objects.published().actual(), slug=kwargs['slug']
        )
        article.show_subscribe = list_page.show_subscribe
        article.subscribe_block = list_page.subscribe_block

        kwargs.update(
            page=article,
            list_page=list_page,
            sections=article.sections.published(),
            published_status=StatusChoices.PUBLIC.value
        )
        return kwargs


class BlogView(LangViewMixin, BaseTemplateView):
    """Страница блога"""

    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        kwargs = super(BlogView, self).get_context_data(**kwargs)
        page = models.BlogPage.get_solo()
        articles = models.Article.objects.published().actual()

        # pagination
        page_index = self.request.GET.get('page', '')

        try:
            page_index = int(page_index)
        except ValueError:
            page_index = 1
        paginator = None
        p = Paginator(articles, ARTICLES_PER_PAGE, allow_empty_first_page=False)
        try:
            paginator = p.page(page_index)
            articles = paginator.object_list
        except (EmptyPage, InvalidPage):
            articles = tuple()

        kwargs.update(
            page=page,
            articles=articles,
            page_index=page_index,
            paginator=paginator
        )
        return kwargs
