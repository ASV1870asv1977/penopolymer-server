from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, InlinePanel, FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    """Главная"""

    max_count = 1
    subpage_types = [
        'products.ProductsIndexPage',
        'about.AboutPage',
        'contacts.ContactsPage',
        'library.LibraryPage',
        'gallery.GalleryPage',
        'questions.QuestionsPage',
        'forms.FormsPage',
        'calendars.CalendarsPage',
    ]
    parent_page_types = []

    article_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='изображение'
    )

    article_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='название статьи',
    )

    article = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        blank=True,
        null=True,
        verbose_name='текст статьи',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('slides', label='слайд')],
            heading='Слайды'),
        MultiFieldPanel([
            ImageChooserPanel('article_image'),
            FieldPanel('article_title'),
            FieldPanel('article'),
        ],
            heading='Статья'),
    ]


class HomeSlidesImage(Orderable):
    """Изображения продукции для слайдов с описанием"""
    image_slide = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Изображение продукции',
    )

    product_name = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Название продукции",
    )

    product_description = RichTextField(
        features=['enter'],
        blank=True,
        null=True,
        max_length=200,
        verbose_name="Описание продукции",
    )

    equipment = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='slides',
    )

    panels = [
        ImageChooserPanel('image_slide'),
        FieldPanel('product_name'),
        FieldPanel('product_description'),
    ]
