# Generated by Django 4.2.3 on 2023-10-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_amount_saled_product_amount_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(default='path_to_static/No_image_available.svg', upload_to='path_to_media', verbose_name='Превью'),
        ),
    ]
