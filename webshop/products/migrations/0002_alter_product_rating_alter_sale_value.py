# Generated by Django 4.2.3 on 2023-07-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='value',
            field=models.PositiveSmallIntegerField(verbose_name='Размер скидки'),
        ),
    ]
