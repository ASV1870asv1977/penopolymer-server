from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.models import Page


class ContactsPage(Page):
    """Страница Контакты"""
    max_count = 1

    subpage_types = []
    parent_page_types = ['home.HomePage']

    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Адрес")
    telephones = models.CharField(max_length=100, blank=True, null=True, verbose_name="Телефоны")
    fax = models.CharField(max_length=100, blank=True, null=True, verbose_name="Факс")
    site_1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Сайт")
    site_2 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Сайт")
    email = models.EmailField(verbose_name="Электронная почта")

    dealer_address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Адрес дилеров")
    dealer_site = models.CharField(max_length=200, blank=True, null=True, verbose_name="Сайт дилеров")
    dealer_email = models.EmailField(verbose_name="Электронная почта дилеров")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('telephones'),
            FieldPanel('fax'),
            FieldPanel('site_1'),
            FieldPanel('site_2'),
            FieldPanel('email'),

        ],
            heading='Контакты'),
        MultiFieldPanel([
            FieldPanel('dealer_address'),
            FieldPanel('dealer_site'),
            FieldPanel('dealer_email'),
        ],
            heading='Контакты дилеров'),
    ]

