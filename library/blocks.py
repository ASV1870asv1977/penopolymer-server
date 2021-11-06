from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class IconCaptionBlock(StructBlock):

    icon = ImageChooserBlock(label='Тип документа')
    caption = CharBlock(label='Название документа')

    class Meta:
        template = 'blocks/icon_caption_block.html'
        label = 'Тип документа с названием документа'


class DocDescriptionBlock(StructBlock):

    icon = ImageChooserBlock(label='Тип документа')
    caption = CharBlock(label='Название документа')
    description = RichTextBlock(label='Описание документа')

    class Meta:
        template = 'blocks/doc_description_block.html'
        label = 'Тип документа с названием документа и описанием'
