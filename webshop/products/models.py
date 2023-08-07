from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    preview = models.ImageField(upload_to='path_to_static', verbose_name='Превью')

    class Meta:
        ordering = ['name']
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    preview = models.ImageField(upload_to='path_to_media', verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    official_name = models.CharField(max_length=200, verbose_name='Зарегистрированное имя')
    licence = models.BooleanField(default=False, verbose_name='Лицензия')

    class Meta:
        ordering = ['name', 'official_name']
        verbose_name='Бренд'
        verbose_name_plural='Бренды'

    def __str__(self) -> str:
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    preview = models.ImageField(upload_to='path_to_media', verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    official_name = models.CharField(max_length=200, verbose_name='Зарегистрированное имя')
    licence = models.BooleanField(default=False, verbose_name='Лицензия')

    class Meta:
        ordering = ['name', 'official_name']
        verbose_name='Продавец'
        verbose_name_plural='Продавцы'

    def __str__(self) -> str:
        return self.name

class Sale(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    value = models.PositiveSmallIntegerField(verbose_name='Размер скидки')
    preview = models.ImageField(upload_to='path_to_media', verbose_name='Превью')
    start_date = models.DateTimeField(verbose_name='Дата добавления')
    end_date = models.DateTimeField(verbose_name='Дата окончания')

    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]
        ordering = ['-start_date']
        verbose_name='Скидка'
        verbose_name_plural='Скидки'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, verbose_name='Бренд', null=True, blank=True)
    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    sale = models.ForeignKey(to=Sale, on_delete=models.PROTECT, verbose_name='Скидка', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')
    short_description = models.CharField(max_length=53, verbose_name='Описание', null=True)
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    tags = TaggableManager(blank=True, verbose_name='Теги')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def verbose_description(self):
        if len(self.description) <= 50:
            return self.description
        return f'{self.description[:50]}...'

    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]
        default_related_name = 'products'
        ordering = ['-created']
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def __str__(self) -> str:
        return self.name
    
    def save(self):
        super().save()
        self.short_description = self.verbose_description()
        super().save()

class Image(models.Model):
    product = models.ForeignKey(to=Product, related_name='images', on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='path_to_media', verbose_name='Путь к изображению')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        ordering = ['-product__pk']
        verbose_name='Изображение'
        verbose_name_plural='Изображения'

    def __str__(self) -> str:
        return self.image.url
