from django.db import models
from django.contrib.auth.models import User
from . import validators


class UserProfile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=40, validators=[validators.name_validator], verbose_name='Имя')
    surname = models.CharField(max_length=100, validators=[validators.name_validator], verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', null=True)
    email = models.EmailField(verbose_name='Почта')
    avatar = models.ImageField(upload_to='avatars', default='path_to_static/no_image_available.jpg', verbose_name='Фото', null=True, blank=True)
    balance = models.OneToOneField(to="Balance", on_delete=models.CASCADE, related_name='profile', verbose_name='Кошелёк')
    password = models.CharField(max_length=30, verbose_name='Пароль')
    reset_token = models.CharField(max_length=32, null=True, blank=True)
    # cart = models.OneToOneField(to="cart.Cart", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'age']
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self) -> str:
        return self.name


class Balance(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Баланс')

    class Meta:
        ordering = ['value']
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'

    def __str__(self) -> str:
        return f'{self.value}'


class Address(models.Model):
    objects = models.Manager()
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    profile = models.ForeignKey(to="UserProfile", on_delete=models.CASCADE, verbose_name='Аккаунт')
    post_index = models.CharField(max_length=9, verbose_name='Почтовый индекс')
    country = models.CharField(max_length=40, verbose_name='Страна')
    region = models.CharField(max_length=40, verbose_name='Регион')
    city = models.CharField(max_length=40, verbose_name='Город')
    street = models.CharField(max_length=40, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом')
    apartment = models.CharField(max_length=10, verbose_name='Квартира', null=True)

    class Meta:
        ordering = ['country', 'city']
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self) -> str:
        return f'{self.profile} - {self.street},{self.house}'