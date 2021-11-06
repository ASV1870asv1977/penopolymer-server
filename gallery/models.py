from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


# class GalleryImage(Orderable):
#     """Изображения Галереи"""
#
#     photo = models.ForeignKey(
#         'wagtailimages.Image',
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         verbose_name='Фото'
#     )
#     images = ParentalKey(
#         'gallery.GalleryTheme',
#         on_delete=models.CASCADE,
#         related_name='images'
#     )
#     panels = [
#         ImageChooserPanel('photo'),
#     ]


class GalleryTheme(Orderable):
    """Тема Галереи"""

    photo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Фото'
    )

    gallery_theme = ParentalKey(
        'gallery.GalleryPage',
        on_delete=models.CASCADE,
        related_name='gallery_theme',
    )
    panels = [
        ImageChooserPanel('photo'),
    ]


class GalleryPage(Page):
    """Фотографии Галерея"""

    max_count = 1
    subpage_types = []
    parent_page_types = ['home.HomePage']

    gallery_name = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Название темы галереи",
    )

    content_panels = Page.content_panels + [
        FieldPanel(
            'gallery_name',
            heading='Название галереи'
        ),
        MultiFieldPanel(
            [
                InlinePanel('gallery_theme', label='фотографию')
            ],
            heading='Галерея'),
    ]

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
