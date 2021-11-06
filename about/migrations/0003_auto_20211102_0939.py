# Generated by Django 3.2.8 on 2021-11-02 06:39

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20211102_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='name_article_third',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название статьи ч.3'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='article_part_third',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Содержание статьи ч.3'),
        ),
    ]
