# -*- coding: utf-8 -*-
import traceback
from collections import OrderedDict
from json import JSONDecodeError
from typing import Optional, Union

from django.conf import settings
from django.utils.translation import gettext_lazy as _
import requests
import simplejson

from snippets.enumerates import BaseEnumerate


BITRIX_ORDER = 58  # 'Order'
BITRIX_CONSULT = 60  # 'Consult'
BITRIX_ORDER_NEW = 54  # 'New'
BITRIX_ORDER_SENT = 56  # 'Sent'
BITRIX_ORDER_DELIVERED = 62  # 'Delivered'


class Bitrix24LeadSourceEnum(BaseEnumerate):
    """Источники лидов"""
    CALL = 'CALL'
    WEB = 'WEB'

    values = OrderedDict((
        (CALL, _('Колл-центр')),
        (WEB, _('Сайт'))
    ))

    default = WEB


class Bitrix24(object):
    """Обработчик запросов в Bitrix24.ru"""
    def __init__(self, hook_name='site', domain=None, token=None):
        self.domain = domain if domain is not None else settings.BITRIX24_DOMAIN
        self.token = token if token is not None else settings.BITRIX24_TOKENS.get(hook_name, '')
        self.full_domain = 'https://%s.bitrix24.ru/rest/65/%s/' % (self.domain, self.token)

    def call(self, method, data=None):
        data = data if data else {}
        assert isinstance(method, str) and method

        url = '%s%s.json' % (self.full_domain, method)
        result = requests.post(url, json=data)

        return result.json()


def crm_lead_add(title, lead_type=BITRIX_CONSULT, order_status=None,
                 source=Bitrix24LeadSourceEnum.WEB, emails=None, phones=None, comments=None):
    bx24 = Bitrix24()
    data = {
        'fields': {
            'ASSIGNED_BY_ID': 1,
            'OPENED': 'Y',
            'SOURCE_ID': source,
            'STATUS_ID': 'NEW',
            'TITLE': title,
            settings.BITRIX_LEAD_TYPE_FIELD_NAME: lead_type
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if order_status:
        data['fields'][settings.BITRIX_ORDER_STATUS_FIELD_NAME] = order_status

    if phones:
        if not isinstance(phones, (dict, list, tuple, set)):
            phones = [phones]

        data['fields']['PHONE'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in phones
        ]

    if emails:
        if not isinstance(emails, (dict, list, tuple, set)):
            emails = [emails]

        data['fields']['EMAIL'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in emails
        ]

    if comments:
        data['fields']['COMMENTS'] = comments

    return bx24.call('crm.lead.add', data)


def crm_company_add(name: str, phone_number: list, emails: Union[str, list, None] = None) -> dict:
    bx24 = Bitrix24()
    data = {
        'fields': {
            'TITLE': name,
            'COMPANY_TYPE': 'CUSTOMER',
        }
    }
    if phone_number:
        data['fields']['PHONE'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in
            phone_number
        ]
    if emails:
        if not isinstance(emails, (dict, tuple, set)):
            emails = [emails]

        data['fields']['EMAIL'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in
            emails
        ]
    return bx24.call('crm.company.add', data)


def crm_contact_add(name, emails=None, phones=None, comments=None):
    bx24 = Bitrix24()
    data = {
        'fields': {
            'ASSIGNED_BY_ID': 1,
            'EXPORT': 'Y',
            'NAME': name,
            'OPENED': 'Y',
            'SOURCE_ID': 'WEB',
            'STATUS_ID': 'NEW',
            'TYPE_ID': 'CLIENT'
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if phones:
        if not isinstance(phones, (list, tuple, set)):
            phones = [phones]

        data['fields']['PHONE'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in phones
        ]

    if emails:
        if not isinstance(emails, (tuple, set, list)):
            emails = [emails]

        data['fields']['EMAIL'] = [
            {'VALUE': str(x).lower().strip(), 'VALUE_TYPE': 'WORK'} for x in emails
        ]

    if comments:
        data['fields']['COMMENTS'] = comments

    return bx24.call('crm.contact.add', data)


def crm_lead_userfield_list() -> dict:
    bx24 = Bitrix24()

    return bx24.call('crm.lead.userfield.list')


def crm_add_deal(name: str, phone_number: str, email: Optional[str] = None,
                 comment: Optional[str] = None, url: Optional[str] = None,
                 **kwargs):
    bx24 = Bitrix24()

    data = {
        'fields': {
            'ASSIGNED_BY_ID': 1,
            'NAME': name,
            'IS_NEW': 'Y',
            'PROBABILITY': 100,
            'TITLE': f'Заявка от {name} ({phone_number})',
            "STAGE_ID": 'NEW'
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    company = crm_company_add(name, [phone_number], emails=email)
    contact = crm_contact_add(
        name,
        emails=[email] if email else None,
        phones=[phone_number],
        comments=comment
    )

    if company and not company.get('error'):
        data['fields']['COMPANY_ID'] = company['result']

    if contact and not contact.get('error'):
        data['fields']['CONTACT_ID'] = contact['result']

    if comment:
        data['fields']['COMMENTS'] = comment

    try:
        return bx24.call('crm.deal.add', data)
    except (
        JSONDecodeError, simplejson.JSONDecodeError,
        requests.exceptions.RequestException, ConnectionError
    ) as e:
        print(e)
        traceback.print_exc()
        return None
