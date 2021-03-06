# Generated by Django 3.2.8 on 2021-11-02 12:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20211102_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarypage',
            name='document_description',
            field=wagtail.core.fields.StreamField([('docdescriptionblock', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(label='Тип документа')), ('caption', wagtail.core.blocks.CharBlock(label='Название документа')), ('description', wagtail.core.blocks.RichTextBlock(label='Описание документа'))]))], blank=True, verbose_name='Документация с описанием'),
        ),
        migrations.AlterField(
            model_name='librarypage',
            name='document_list',
            field=wagtail.core.fields.StreamField([('iconcaptionblock', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(label='Тип документа')), ('caption', wagtail.core.blocks.CharBlock(label='Название документа'))]))], blank=True, verbose_name='Список документации'),
        ),
    ]
