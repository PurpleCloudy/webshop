# Generated by Django 4.2.3 on 2023-09-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_address_options_alter_balance_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=30, verbose_name='Пароль'),
        ),
    ]
