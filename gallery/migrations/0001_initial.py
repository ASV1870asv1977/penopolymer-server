# Generated by Django 3.2.8 on 2021-11-02 13:48

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GalleryTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('gallery_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название темы галереи')),
                ('image_list', wagtail.core.fields.StreamField([('image_block', wagtail.images.blocks.ImageChooserBlock(template='blocks/gallery_image_block.html'))], blank=True, verbose_name='Фотография')),
                ('gallery_theme', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_theme', to='gallery.gallerypage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
