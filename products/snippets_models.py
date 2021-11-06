from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class TableDataProduct1(Orderable):
    """Данные в таблицу характеристик труб"""

    product_brand = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        verbose_name="Название продукции",
    )
    diameter_nominal = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр условный трубопровода, Ду",
    )
    diameter_outside = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр наружный трубопровода, Дтр",
    )
    diameter_insulation = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр изоляции, Диз",
    )
    insulation_thickness = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Толщина изоляции, ?из",
    )
    insulation_mass = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Масса 1пм. изоляции, кг",
    )
    product = ParentalKey(
        'products.TablePageProduct1',
        on_delete=models.CASCADE,
        related_name='product_1_data',
    )
    panels = [
        FieldPanel('product_brand'),
        FieldPanel('diameter_nominal'),
        FieldPanel('diameter_outside'),
        FieldPanel('diameter_insulation'),
        FieldPanel('insulation_thickness'),
        FieldPanel('insulation_mass'),
    ]


@register_snippet
class TablePageProduct1(ClusterableModel):
    """Фрагмент с таблицей характеристик труб"""

    panels = [
        MultiFieldPanel([
            InlinePanel('product_1_data', label='изделие')],
            heading='Характеристики труб'),
    ]

    class Meta:
        verbose_name = 'Характеристики труб'
        verbose_name_plural = 'Характеристики труб'

    def __str__(self):
        return 'Характеристики труб'


class TableDataProduct2(Orderable):
    """Данные в таблицу характеристик отводов"""

    product_brand = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        verbose_name="Название продукции",
    )
    diameter_nominal = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр условный трубопровода, Ду",
    )
    diameter_outside = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр наружный трубопровода, Дтр",
    )
    diameter_insulation = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр изоляции, Диз",
    )
    insulation_thickness = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Толщина изоляции, ?из",
    )
    bend_radius = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Радиус отвода, R",
    )
    lever_arm_length = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Длина плеча отвода, L",
    )
    theoretical_mass = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Теоретическая масса отвода 90° в ППМ изоляции, кг",
    )
    product = ParentalKey(
        'products.TablePageProduct2',
        on_delete=models.CASCADE,
        related_name='product_2_data',
    )
    panels = [
        FieldPanel('product_brand'),
        FieldPanel('diameter_nominal'),
        FieldPanel('diameter_outside'),
        FieldPanel('diameter_insulation'),
        FieldPanel('insulation_thickness'),
        FieldPanel('bend_radius'),
        FieldPanel('lever_arm_length'),
        FieldPanel('theoretical_mass'),
    ]


@register_snippet
class TablePageProduct2(ClusterableModel):
    """Фрагмент с таблицей характеристик отводов"""

    panels = [
        MultiFieldPanel([
            InlinePanel('product_2_data', label='изделие')],
            heading='Характеристики отводов'),
    ]

    class Meta:
        verbose_name = 'Характеристики отводов'
        verbose_name_plural = 'Характеристики отводов'

    def __str__(self):
        return 'Характеристики отводов'


class TableDataProduct3(Orderable):
    """Данные в таблицу характеристик шаровых кранов"""

    product_brand = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        verbose_name="Название продукции",
    )
    diameter_nominal = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Условный диаметр, Ду",
    )
    rod_diameter = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр штока, d",
    )
    diameter_insulation = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр изоляции, Диз",
    )
    insulation_thickness = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Толщина изоляции, ?из",
    )
    h_min = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Н мин",
    )
    lever_arm_length = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Длина плеча отвода, L",
    )
    mass = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Масса изолированного шарового крана, кг г",
    )
    product = ParentalKey(
        'products.TablePageProduct3',
        on_delete=models.CASCADE,
        related_name='product_3_data',
    )
    panels = [
        FieldPanel('product_brand'),
        FieldPanel('diameter_nominal'),
        FieldPanel('rod_diameter'),
        FieldPanel('diameter_insulation'),
        FieldPanel('insulation_thickness'),
        FieldPanel('h_min'),
        FieldPanel('lever_arm_length'),
        FieldPanel('mass'),
    ]


@register_snippet
class TablePageProduct3(ClusterableModel):
    """Фрагмент с таблицей характеристик отводов"""

    panels = [
        MultiFieldPanel([
            InlinePanel('product_3_data', label='изделие')],
            heading='Характеристики шаровых кранов'),
    ]

    class Meta:
        verbose_name = 'Характеристики шаровых кранов'
        verbose_name_plural = 'Характеристики шаровых кранов'

    def __str__(self):
        return 'Характеристики шаровых кранов'


class TableDataProduct5(Orderable):
    """Данные в таблицу характеристик неподвижных опор"""

    product_brand = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        verbose_name="Название продукции",
    )
    diameter_nominal = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр условный трубопровода, Ду",
    )
    diameter_outside = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр наружный трубопровода, Dтр",
    )
    diameter_insulation = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Диаметр изоляции, Диз",
    )
    insulation_thickness = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Толщина изоляции, ?из",
    )
    fixed_support_length = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Длина неподвижной опоры",
    )
    distance_between_shields = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Расстояние между щитами, K",
    )
    shield_size = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Размер щита, A",
    )
    maximum_axial_load = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Максимальная осевая нагрузка, тн",
    )
    theoretical_weight = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Теоретическая масса НО в ППМ изоляции 1 шт, кг",
    )
    product = ParentalKey(
        'products.TablePageProduct5',
        on_delete=models.CASCADE,
        related_name='product_5_data',
    )
    panels = [
        FieldPanel('product_brand'),
        FieldPanel('diameter_nominal'),
        FieldPanel('diameter_outside'),
        FieldPanel('diameter_insulation'),
        FieldPanel('insulation_thickness'),
        FieldPanel('fixed_support_length'),
        FieldPanel('distance_between_shields'),
        FieldPanel('shield_size'),
        FieldPanel('maximum_axial_load'),
        FieldPanel('theoretical_weight'),
    ]


@register_snippet
class TablePageProduct5(ClusterableModel):
    """Фрагмент с таблицей характеристик неподвижных опор"""

    panels = [
        MultiFieldPanel([
            InlinePanel('product_5_data', label='изделие')],
            heading='Характеристики неподвижных опор'),
    ]

    class Meta:
        verbose_name = 'Характеристики неподвижных опор'
        verbose_name_plural = 'Характеристики неподвижных опор'

    def __str__(self):
        return 'Характеристики неподвижных опор'
