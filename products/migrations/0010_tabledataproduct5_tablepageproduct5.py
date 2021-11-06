# Generated by Django 3.2.8 on 2021-11-01 19:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_tabledataproduct3_tablepageproduct3'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablePageProduct5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Характеристики неподвижных опор',
                'verbose_name_plural': 'Характеристики неподвижных опор',
            },
        ),
        migrations.CreateModel(
            name='TableDataProduct5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('product_brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='Название продукции')),
                ('diameter_nominal', models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр условный трубопровода, Ду')),
                ('diameter_outside', models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр наружный трубопровода, Dтр')),
                ('diameter_insulation', models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр изоляции, Диз')),
                ('insulation_thickness', models.CharField(blank=True, max_length=10, null=True, verbose_name='Толщина изоляции, ?из')),
                ('fixed_support_length', models.CharField(blank=True, max_length=10, null=True, verbose_name='Длина неподвижной опоры')),
                ('distance_between_shields', models.CharField(blank=True, max_length=10, null=True, verbose_name='Расстояние между щитами, K')),
                ('shield_size', models.CharField(blank=True, max_length=10, null=True, verbose_name='Размер щита, A')),
                ('maximum_axial_load', models.CharField(blank=True, max_length=10, null=True, verbose_name='Максимальная осевая нагрузка, тн')),
                ('theoretical_weight', models.CharField(blank=True, max_length=10, null=True, verbose_name='Теоретическая масса НО в ППМ изоляции 1 шт, кг')),
                ('product', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_5_data', to='products.tablepageproduct5')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]