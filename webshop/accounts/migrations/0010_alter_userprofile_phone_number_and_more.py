# Generated by Django 4.2.3 on 2023-10-19 16:26

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(max_length=100, validators=[accounts.validators.name_validator], verbose_name='Фамилия'),
        ),
    ]
