# Generated by Django 3.2.8 on 2021-11-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211101_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTablePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Характеристики труб',
                'verbose_name_plural': 'Характеристики труб',
            },
        ),
        migrations.AlterField(
            model_name='producttabledata',
            name='diameter_insulation',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр изоляции, Диз'),
        ),
        migrations.AlterField(
            model_name='producttabledata',
            name='diameter_nominal',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр условный трубопровода, Ду'),
        ),
        migrations.AlterField(
            model_name='producttabledata',
            name='diameter_outside',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Диаметр наружный трубопровода, Дтр'),
        ),
        migrations.AlterField(
            model_name='producttabledata',
            name='insulation_mass',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Масса 1пм. изоляции, кг'),
        ),
        migrations.AlterField(
            model_name='producttabledata',
            name='insulation_thickness',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Толщина изоляции, ?из'),
        ),
    ]
