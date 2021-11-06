from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.snippets.models import register_snippet


class EventCard(Orderable):
    """Календарь мероприятий"""
    event_data = models.CharField(max_length=2, verbose_name="Число месяца")
    event_month = models.CharField(max_length=8, verbose_name="Месяц")
    event_name = RichTextField(
        max_length=200,
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        verbose_name="Название мероприятия",
    )
    event_description = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        null=True,
        verbose_name="Описание мероприятия",
    )
    event = ParentalKey(
        'home.EventNewsPages',
        on_delete=models.CASCADE,
        related_name='events',
    )
    panels = [
        FieldPanel('event_data'),
        FieldPanel('event_month'),
        FieldPanel('event_name'),
        FieldPanel('event_description'),
    ]


class NewsCard(Orderable):
    """Новости компании"""
    news_data = models.CharField(max_length=2, verbose_name="Число месяца")
    news_month = models.CharField(max_length=8, verbose_name="Месяц")
    news_name = RichTextField(
        max_length=200,
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        verbose_name="Название новости",
    )
    news_description = RichTextField(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        null=True,
        verbose_name="Описание новости",
    )
    news = ParentalKey(
        'home.EventNewsPages',
        on_delete=models.CASCADE,
        related_name='news',
    )
    panels = [
        FieldPanel('news_data'),
        FieldPanel('news_month'),
        FieldPanel('news_name'),
        FieldPanel('news_description'),
    ]


@register_snippet
class EventNewsPages(ClusterableModel):
    """Блок с календарем мероприятий и новостями"""
    panels = [
        MultiFieldPanel(
            [InlinePanel('events', label='мероприятие')],
            heading='Мероприятия'),
        MultiFieldPanel(
            [InlinePanel('news', label='новость')],
            heading='Новости'),
    ]

    class Meta:
        verbose_name = 'Новости и мероприятия'
        verbose_name_plural = 'Новости и мероприятия'

    def __str__(self):
        return 'Новости и мероприятия'


class ProductCard(Orderable):
    """Карточка продукции"""
    product_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='изображение'
    )

    product_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название продукции",
    )

    path_to_page = models.CharField(
        max_length=50,
        null=True,
        verbose_name="Заголовок страницы продукции",
    )

    product_description = RichTextField(
        features=['enter'],
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Описание продукции",
    )

    equipment = ParentalKey(
        'home.ProductCardPages',
        on_delete=models.CASCADE,
        related_name='products',
    )

    panels = [
        ImageChooserPanel('product_image'),
        FieldPanel('product_name'),
        FieldPanel('path_to_page'),
        FieldPanel('product_description'),
    ]


@register_snippet
class ProductCardPages(ClusterableModel):
    panels = [
        MultiFieldPanel(
            [InlinePanel('products', label='карточку продукции')],
            heading='Продукция'),
    ]

    class Meta:
        verbose_name = 'Карточка продукции'
        verbose_name_plural = 'Карточки продукции'

    def __str__(self):
        return 'Карточки продукции'


@register_snippet
class Header(models.Model):
    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    panels = [
        FieldPanel('telephones'),
        FieldPanel('address'),
    ]

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'

    def __str__(self):
        return 'Хедер'


@register_snippet
class Footer(models.Model):
    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    email = models.EmailField(
        verbose_name="Email предприятия",
    )

    panels = [
        FieldPanel('address'),
        FieldPanel('telephones'),
        FieldPanel('email'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'
