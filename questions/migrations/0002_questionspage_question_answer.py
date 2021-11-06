# Generated by Django 3.2.8 on 2021-11-03 07:41

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionspage',
            name='question_answer',
            field=wagtail.core.fields.StreamField([('question_answer_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(label='Вопрос')), ('description', wagtail.core.blocks.RichTextBlock(label='Ответ'))]))], blank=True, verbose_name='Документация с описанием'),
        ),
    ]
