from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock


class QuestionAnswerBlock(StructBlock):

    question = RichTextBlock(label='Вопрос')
    answer = RichTextBlock(label='Ответ')

    class Meta:
        label = 'Вопрос с ответом'
