from django.utils.text import slugify
from django.shortcuts import get_object_or_404
import datetime
import pytz
from . import models, views_decorators

def update_product_data(product:models.Product, data:dict) -> None:
    if 'category' in data.keys():
        product.category = get_object_or_404(models.Category, id=data['category']['id'])
    if 'brand' in data.keys():
        product.brand = get_object_or_404(models.Brand, id=data['brand']['id'])
    if 'seller' in data.keys():
        product.seller = get_object_or_404(models.Seller, id=data['seller']['id'])
    if 'sale' in data.keys():
        product.sale = get_object_or_404(models.Sale, id=data['sale']['id'])
    if 'name' in data.keys():
        product.name = data['name']
        product.slug = slugify(product.name)
    if 'description' in data.keys():
        product.description = data['description']
    if 'rating' in data.keys():
        product.rating = data['rating']
    if 'price' in data.keys():
        product.price = data['price']
    if 'tags' in data.keys():
        product.tags.remove()
        for tag in data['tags']:
            product.tags.add(tag)
    product.save()

def image_adding(product:models.Product, url:str, description:str) -> int:
    image_obj = models.Image.objects.create(product=product, image=url, description=description)
    image_obj.save()
    return image_obj.pk

def update_sale_data(sale:models.Sale, data:dict) -> None:
    if 'name' in data.keys():
        sale.name = data['name']
    if 'value' in data.keys():
        sale.value = data['value']
    if 'preview' in data.keys():
        sale.preview = data['preview']
    if 'start_date' in data.keys():
        sale.start_date = datetime.datetime.strptime(data['start_date'], '%H:%M:%S %d-%m-%Y')
    if 'end_date' in data.keys():
        sale.end_date = datetime.datetime.strptime(data['end_date'], '%H:%M:%S %d-%m-%Y')
    sale.save()

def update_brand_data(brand:models.Brand, data:dict) -> None:
    if 'name' in data.keys():
        brand.name = data['name']
        brand.slug = slugify(brand.name)
    if 'preview' in data.keys():
        brand.preview = data['preview']
    if 'description' in data.keys():
        brand.description = data['description']
    if 'official_name' in data.keys():
        brand.official_name = data['official_name']
    if 'licence' in data.keys():
        brand.licence = data['licence']
    brand.save()

def update_seller_data(seller:models.Seller, data:dict) -> None:
    if 'name' in data.keys():
        seller.name = data['name']
        seller.slug = slugify(seller.name)
    if 'preview' in data.keys():
        seller.preview = data['preview']
    if 'description' in data.keys():
        seller.description = data['description']
    if 'official_name' in data.keys():
        seller.official_name = data['official_name']
    if 'licence' in data.keys():
        seller.licence = data['licence']
    seller.save()