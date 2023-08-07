from django.contrib import admin
from . import models

class ProductImageInline(admin.TabularInline):
    model = models.Image
    extra = 5


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'price', 'sale', 'rating', 'tags', 'category', 'seller', 'brand', 'created', 'short_description']
    list_filter = ['created']
    prepopulated_fields = {'slug': ['name']}
    exclude = ['short_description']
    inlines = [ProductImageInline]

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'official_name', 'licence', 'preview', 'description']
    list_filter = ['name']
    prepopulated_fields = {'slug': ['name']}

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'preview']
    list_filter = ['name']
    prepopulated_fields = {'slug': ['name']}

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image', 'description']

@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value', 'start_date', 'end_date', 'preview']
    list_filter = ['start_date']

@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'official_name', 'licence', 'preview', 'description']
    list_filter = ['name']
    prepopulated_fields = {'slug': ['name']}
