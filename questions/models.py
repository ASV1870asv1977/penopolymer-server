from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import MultiFieldPanel, StreamFieldPanel, FieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page

from questions.blocks import QuestionAnswerBlock


class FormField(AbstractFormField):

    page = ParentalKey(
        'QuestionsPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class QuestionsPage(AbstractEmailForm):
    """Страница Вопросы и ответы"""

    max_count = 1
    subpage_types = []
    parent_page_types = ['home.HomePage']

    question_answer = StreamField(
        [
            ('question_answer_block', QuestionAnswerBlock()),
        ],
        blank=True,
        verbose_name='Документация с описанием',
    )

    intro = RichTextField(
        blank=True,
        verbose_name='Предварительный текст',
    )
    thank_you_text = RichTextField(
        blank=True,
        verbose_name='Текст после отправки формы',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('question_answer')],
            heading='Вопросы и ответы'),
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Поля формы для отправки вопроса'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading='Настройки электронной почты'),
    ]
