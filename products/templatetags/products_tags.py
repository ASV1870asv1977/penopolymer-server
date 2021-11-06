from django import template
from products.snippets_models import TablePageProduct1, TablePageProduct2, TablePageProduct3, TablePageProduct5

register = template.Library()


@register.inclusion_tag('products/tables_tags/product_1_table.html', takes_context=True)
def product_1_table_tag(context):
    return {
        'request': context['request'],
        'product_1': TablePageProduct1.objects.first(),
    }


@register.inclusion_tag('products/tables_tags/product_2_table.html', takes_context=True)
def product_2_table_tag(context):
    return {
        'request': context['request'],
        'product_2': TablePageProduct2.objects.first(),
    }


@register.inclusion_tag('products/tables_tags/product_3_table.html', takes_context=True)
def product_3_table_tag(context):
    return {
        'request': context['request'],
        'product_3': TablePageProduct3.objects.first(),
    }


@register.inclusion_tag('products/tables_tags/product_5_table.html', takes_context=True)
def product_5_table_tag(context):
    return {
        'request': context['request'],
        'product_5': TablePageProduct5.objects.first(),
    }
