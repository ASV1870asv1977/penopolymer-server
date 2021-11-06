# Generated by Django 3.2.8 on 2021-11-01 09:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0003_auto_20211101_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNewsPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Новости и мероприятия',
                'verbose_name_plural': 'Новости и мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Адрес предприятия')),
                ('telephones', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Телефоны предприятия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email предприятия')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футеры',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephones', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Телефоны предприятия')),
                ('address', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Адрес предприятия')),
            ],
            options={
                'verbose_name': 'Хедер',
                'verbose_name_plural': 'Хедеры',
            },
        ),
        migrations.CreateModel(
            name='ProductCardPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Карточка продукции',
                'verbose_name_plural': 'Карточки продукции',
            },
        ),
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название продукции')),
                ('product_description', wagtail.core.fields.RichTextField(blank=True, max_length=200, null=True, verbose_name='Описание продукции')),
                ('equipment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.productcardpages')),
                ('product_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='изображение')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('news_data', models.CharField(max_length=2, verbose_name='Число месяца')),
                ('news_month', models.CharField(max_length=8, verbose_name='Месяц')),
                ('news_name', wagtail.core.fields.RichTextField(max_length=200, null=True, verbose_name='Название новости')),
                ('news_description', wagtail.core.fields.RichTextField(null=True, verbose_name='Описание новости')),
                ('news', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='home.eventnewspages')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('event_data', models.CharField(max_length=2, verbose_name='Число месяца')),
                ('event_month', models.CharField(max_length=8, verbose_name='Месяц')),
                ('event_name', wagtail.core.fields.RichTextField(max_length=200, null=True, verbose_name='Название мероприятия')),
                ('event_description', wagtail.core.fields.RichTextField(null=True, verbose_name='Описание мероприятия')),
                ('event', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='home.eventnewspages')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
