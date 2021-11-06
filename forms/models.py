from django.db import models
from wagtail.core.models import Page


class FormsPage(Page):
    """Страница Создание заявки"""
    max_count = 1
    subpage_types = []
    parent_page_types = ['home.HomePage']
