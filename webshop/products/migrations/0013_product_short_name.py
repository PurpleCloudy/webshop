# Generated by Django 4.2.3 on 2023-11-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_feedback_number_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_name',
            field=models.CharField(max_length=33, null=True, verbose_name='Краткое имя'),
        ),
    ]
