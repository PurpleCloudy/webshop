from . import models


def serialize_category(category:models.Category):
    current_category_data = {
    'id':category.pk,
    'name':category.name,
    'slug':category.slug,
    'preview':category.preview.url,
    }
    return current_category_data


def serialize_brand(brand:models.Brand):
    current_brand_data = {
        'name':brand.name,
        'slug':brand.slug,
        'preview':brand.preview.url,
        'description':brand.description,
        'official_name':brand.official_name,
        'licence':brand.licence,
    }
    return current_brand_data

def serialize_seller(seller:models.Seller):
    current_seller_data = {
        'name':seller.name,
        'slug':seller.slug,
        'preview':seller.preview.url,
        'description':seller.description,
        'official_name':seller.official_name,
        'licence':seller.licence,
    }
    return current_seller_data

def serialize_sale(sale:models.Sale):
    current_sale_data = {
        'id':sale.pk,
        'name':sale.name,
        'value':sale.value,
        'preview':sale.preview.url,
        'start_date':sale.start_date,
        'end_date':sale.end_date,
    }
    return current_sale_data

def serialize_image(image:models.Image):
    current_image_data = {
                'id':image.pk,
                'url':image.image.url,
                'description':image.description,
            }
    return current_image_data

def serialize_product_obj(product:models.Product) -> dict:
    current_product_data = {
        'id':product.pk,
        'category':serialize_category(product.category),
        'brand':serialize_brand(product.brand),
        'seller':serialize_seller(product.seller),
        'name':product.name,
        'slug':product.slug,
        'description':product.description,
        'rating':product.rating,
        'price':product.price,
        'created':product.created,
        'images':[
            serialize_image(image) for image in models.Image.objects.filter(product=product)
        ]
    }
    if product.sale:
        current_product_data['sale'] = serialize_sale(product.sale)
    if product.tags:
        current_product_data['tags'] = list(product.tags.names())
    return current_product_data