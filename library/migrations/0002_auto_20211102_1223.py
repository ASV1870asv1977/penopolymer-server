# Generated by Django 3.2.8 on 2021-11-02 09:23

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarypage',
            name='document_description',
            field=wagtail.core.fields.StreamField([('docdescriptionblock', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(label='Тип документа')), ('caption', wagtail.core.blocks.CharBlock(label='Название документа')), ('description', wagtail.core.blocks.RichTextBlock(label='Описание документа'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='librarypage',
            name='subtitle_second',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Второй подзаголовок'),
        ),
    ]
