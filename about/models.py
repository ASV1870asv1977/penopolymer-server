from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class AboutPage(Page):
    """Страница О компании"""
    max_count = 1

    subpage_types = []
    parent_page_types = ['home.HomePage']

    article_image_first = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='первое изображение'
    )

    article_image_second = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='второе изображение'
    )

    article_image_third = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='третье изображение'
    )

    article = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        blank=True,
        null=True,
        verbose_name="Содержание статьи ч.1",
    )

    article_part_two = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        blank=True,
        null=True,
        verbose_name="Содержание статьи ч.2",
    )

    name_article_third = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Название статьи ч.3",
    )

    article_part_third = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        blank=True,
        null=True,
        verbose_name="Содержание статьи ч.3",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('article_image_first'),
            ImageChooserPanel('article_image_second'),
            FieldPanel('article'),
            FieldPanel('article_part_two'),
            FieldPanel('name_article_third'),
            ImageChooserPanel('article_image_third'),
            FieldPanel('article_part_third'),
        ],
            heading='Статья'),
    ]

