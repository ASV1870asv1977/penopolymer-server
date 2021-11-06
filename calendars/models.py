from django.db import models
from wagtail.core.models import Page


class CalendarsPage(Page):
    """Страница Календарь"""

    max_count = 1
    subpage_types = []
    parent_page_types = ['home.HomePage']
