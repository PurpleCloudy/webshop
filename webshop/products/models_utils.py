from django.utils.text import slugify
import datetime
from . import models

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
        brand.slug = slugify(data['name'])
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
        seller.slug = slugify(data['name'])
    if 'preview' in data.keys():
        seller.preview = data['preview']
    if 'description' in data.keys():
        seller.description = data['description']
    if 'official_name' in data.keys():
        seller.official_name = data['official_name']
    if 'licence' in data.keys():
        seller.licence = data['licence']
    seller.save()