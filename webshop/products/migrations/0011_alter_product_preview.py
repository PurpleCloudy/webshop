# Generated by Django 4.2.3 on 2023-10-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(default='path_to_static/no_image_available.jpg', upload_to='path_to_media', verbose_name='Превью'),
        ),
    ]
