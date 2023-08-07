from django.views import View
from django.http import JsonResponse, HttpRequest
import json
from . import models
from . import serializers

class SalesAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        sales_qs = models.Sale.objects.all()
        response_data = []
        for sale in sales_qs:
            current_sale_data = serializers.serialize_sale(sale)
            response_data.append(current_sale_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
class ProductAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        products_qs = models.Product.objects.all()
        response_data = []
        for product in products_qs:
            current_product_data = serializers.serialize_product_obj(product)
            response_data.append(current_product_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data = json.loads(request)
        product = models.Product(
            category=data['category'],
            brand=data['brand'],
            seller=data['seller'],
            sale=data['sale'],
            name=data['name'],
            slug=data['slug'],
            description=data['description'],
            rating=data['rating'],
            price=data['price'],
        )
        product.save()
        for img in data['images']:
            new_img = models.Image(
                product=product,
                image=img['path'],
                description=img['description'],
            )
            new_img.save()
        return JsonResponse(data=serializers.serialize_product_obj(product), safe=False, status=200)
    
class BrandAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        brands_qs = models.Brand.objects.all()
        response_data = []
        for brand in brands_qs:
            current_brand_data = serializers.serialize_brand(brand)
            response_data.append(current_brand_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
class SellerAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        sellers_qs = models.Seller.objects.all()
        response_data = []
        for seller in sellers_qs:
            current_seller_data = serializers.serialize_brand(seller)
            response_data.append(current_seller_data)
        return JsonResponse(data=response_data, safe=False, status=200)