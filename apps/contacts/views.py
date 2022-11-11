from contacts import models
from snippets.views import BaseTemplateView, LangViewMixin


class ContactsView(LangViewMixin, BaseTemplateView):
    """Страница контактов"""

    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ContactsView, self).get_context_data(**kwargs)
        page = models.ContactsPage.get_solo()
        kwargs.update(
            page=page,
            contact_blocks=page.contact_blocks.published()
        )
        return kwargs
