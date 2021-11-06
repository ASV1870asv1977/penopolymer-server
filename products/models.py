from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class ProductsIndexPage(Page):
    """Страница для выведения списка продукции"""

    max_count = 1

    subpage_types = ['products.ProductPage']
    parent_page_types = ['home.HomePage']


class ProductPage(Page):
    """Страница продукта"""

    parent_page_types = ['products.ProductsIndexPage']

    product_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    product_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='изображение'
    )

    product_description = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        blank=True,
        null=True,
        verbose_name='описание продукции'
    )

    content_panels = Page.content_panels + [
        FieldPanel('product_name'),
        ImageChooserPanel('product_image'),
        FieldPanel('product_description'),
    ]
