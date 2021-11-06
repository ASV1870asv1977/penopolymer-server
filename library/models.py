from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from library.blocks import IconCaptionBlock, DocDescriptionBlock


class LibraryPage(Page):
    """Страница Библиотека"""
    max_count = 1
    subpage_types = []
    parent_page_types = ['home.HomePage']

    subtitle_first = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Первый подзаголовок',
    )

    document_list = StreamField(
        [
            ('iconcaptionblock', IconCaptionBlock()),
        ],
        blank=True,
        verbose_name='Список документации',
    )

    subtitle_second = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Второй подзаголовок',
    )

    document_description = StreamField(
        [
            ('docdescriptionblock', DocDescriptionBlock()),
        ],
        blank=True,
        verbose_name='Документация с описанием',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle_first'),
            StreamFieldPanel('document_list')],
            heading='Список документации'),
        MultiFieldPanel([
            FieldPanel('subtitle_second'),
            StreamFieldPanel('document_description')],
            heading='Документация с описанием'),
    ]
