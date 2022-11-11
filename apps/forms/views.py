from copy import deepcopy

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import requests

from forms import forms
from integration import bitrix24
from snippets.http.response import success_response, validation_error_response
from snippets.utils.email import send_trigger_email
from snippets.views import BaseView


class BaseFormRequestView(BaseView):
    """Базовый класс запросов клиентов """

    check_recaptcha = not settings.DEBUG
    success_message = _('Спасибо, ваш запрос отправлен!')
    form = None

    def get_event_name(self, request, obj):
        return 'новая отправка формы "%s"' % obj._meta.verbose_name

    def success_trigger(self, request, obj, form):
        pass

    def post(self, request, **kwargs):
        data = deepcopy(request.POST)
        form = self.form(data)

        if not form.is_valid():
            return validation_error_response(form.errors)

        if self.check_recaptcha:
            captcha = request.POST.get('g-recaptcha-response', '')
            if not captcha:
                return validation_error_response({'g-recaptcha-response': [
                    str(_(
                        'Не была проведена проверка на робота. '
                        'Повторите попытку.'
                    ))
                ]})

            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': settings.RECAPTCHA_SECRET,
                    'response': captcha,
                    'remoteip': request.META.get('REMOTE_ADDR', '')
                })
            res = r.json()

            if not res.get('success', False):
                return validation_error_response({'g-recaptcha-response': [
                    str(_('Вы не прошли проверку на робота.'))
                ]})

        obj = form.save()

        event = self.get_event_name(request, obj)
        send_trigger_email(event, request=request, obj=obj, fields=obj.email_fields)

        self.success_trigger(request, obj, form)

        return success_response(self.success_message)


class FeedbackView(BaseFormRequestView):
    """Форма обратной связи"""

    form = forms.FeedbackForm
    success_message = _('Спасибо, сообщение отправлено!')

    def get_event_name(self, request, obj):
        return _('Сообщение обратной связи')

    def success_trigger(self, request, obj, form):
        super(FeedbackView, self).success_trigger(request, obj, form)
        deal = bitrix24.crm_add_deal(**form.cleaned_data)
        print(deal)


class OrderView(BaseFormRequestView):
    """Форма заказа"""

    form = forms.OrderForm
    success_message = _('Спасибо, сообщение отправлено!')

    def get_event_name(self, request, obj):
        return _('Заказ')

    def success_trigger(self, request, obj, form):
        super(OrderView, self).success_trigger(request, obj, form)
        deal = bitrix24.crm_add_deal(**form.cleaned_data)
        print(deal)


class SubscribeView(BaseFormRequestView):
    """Форма заявки на подписку"""

    check_recaptcha = False
    form = forms.SubscribeForm
    success_message = _('Спасибо, подписка оформлена!')

    def get_event_name(self, request, obj):
        return _('Подписка')
