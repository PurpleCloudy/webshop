from django.views import View
from django.http import JsonResponse, HttpRequest
from django.utils.decorators import method_decorator
import json
import datetime
from . import models, serializers, models_utils, views_decorators

class SalesAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        sales_qs = models.Sale.objects.all()
        response_data = []
        for sale in sales_qs:
            current_sale_data = serializers.serialize_sale(sale)
            response_data.append(current_sale_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        try:
            sale = models.Sale(
                name = data['name'], 
                value = data['value'],
                preview = data['preview'],
                start_date = datetime.datetime.strptime(data['start_date'], '%H:%M:%S %d-%m-%Y'),
                end_date = datetime.datetime.strptime(data['end_date'], '%H:%M:%S %d-%m-%Y'),
            )
            sale.save()
            return JsonResponse(data=serializers.serialize_sale(sale), status=201)
        except Exception:
            return JsonResponse(data={'error':'Неверные данные'}, status=400)
    
@method_decorator(views_decorators.check_obj_does_not_exist, name='dispatch')
class SaleAPIView(View):
    def get(self, request:HttpRequest, pk:int) -> JsonResponse:
        sale = models.Sale.objects.get(id=pk)
        return JsonResponse(data=serializers.serialize_sale(sale), status=200)

    def put(self, request:HttpRequest, pk:int) -> JsonResponse:
        data = json.loads(request.body)
        sale = models.Sale.objects.get(id=pk)
        try:
            models_utils.update_sale_data(sale, data)
        except ValueError:
            return JsonResponse(data={'error':'Дата начала больше или равна дате окончания'}, status=400)
        return JsonResponse(data=serializers.serialize_sale(sale), status=200)
    
    def delete(self, request:HttpRequest, pk:int) -> JsonResponse:
        sale = models.Sale.objects.get(id=pk)
        sale.delete()
        return JsonResponse(data={'result':'Успешно удалено'}, status=200)
        
class ProductAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        products_qs = models.Product.objects.all()
        response_data = []
        for product in products_qs:
            current_product_data = serializers.serialize_product_obj(product)
            response_data.append(current_product_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
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
    
class BrandsAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        brands_qs = models.Brand.objects.all()
        response_data = []
        for brand in brands_qs:
            current_brand_data = serializers.serialize_brand(brand)
            response_data.append(current_brand_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        try:
            brand = models.Brand(
                name = data['name'],
                slug = data['slug'],
                preview = data['preview'],
                desc = data['description'],
                official_name = data['official_name'],
                licence = data['licence'],
            )
            brand.save()
            return JsonResponse(data=serializers.serialize_brand(brand), status=201)
        except Exception:
            return JsonResponse(data={'error':'Неверные данные'}, status=400)

@method_decorator(views_decorators.check_obj_does_not_exist, name='dispatch')
class BrandAPIView(View):
    def get(self, request:HttpRequest, pk:int) -> JsonResponse:
        brand = models.Brand.objects.get(id=pk)
        return JsonResponse(data=serializers.serialize_brand(brand), status=200)
    
    def put(self, request:HttpRequest, pk:int) -> JsonResponse:
        data = json.loads(request.body)
        brand = models.Brand.objects.get(id=pk)
        models_utils.update_brand_data(brand, data)
        return JsonResponse(data=serializers.serialize_brand(brand), status=200)

    def delete(self, request:HttpRequest, pk:int) -> JsonResponse:
        brand = models.Brand.objects.get(id=pk)
        brand.delete()
        return JsonResponse(data={'result':'Успешно удалено'}, status=200)

class SellersAPIView(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        sellers_qs = models.Seller.objects.all()
        response_data = []
        for seller in sellers_qs:
            current_seller_data = serializers.serialize_brand(seller)
            response_data.append(current_seller_data)
        return JsonResponse(data=response_data, safe=False, status=200)
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        try:
            seller = models.Seller(
                name = data['name'],
                slug = data['slug'],
                preview = data['preview'],
                desc = data['description'],
                official_name = data['official_name'],
                licence = data['licence'],
            )
            seller.save()
            return JsonResponse(data=serializers.serialize_seller(seller), status=201)
        except Exception:
            return JsonResponse(data={'error':'Неверные данные'}, status=400)

@method_decorator(views_decorators.check_obj_does_not_exist, name='dispatch')
class SellerAPIView(View):
    def get(self, request:HttpRequest, pk:int) -> JsonResponse:
        seller = models.Seller.objects.get(id=pk)
        return JsonResponse(data=serializers.serialize_seller(seller), status=200)
    
    def put(self, request:HttpRequest, pk:int) -> JsonResponse:
        data = json.loads(request.body)
        seller = models.Seller.objects.get(id=pk)
        models_utils.update_seller_data(seller, data)
        return JsonResponse(data=serializers.serialize_seller(seller), status=200)

    def delete(self, request:HttpRequest, pk:int) -> JsonResponse:
        seller = models.Seller.objects.get(id=pk)
        seller.delete()
        return JsonResponse(data={'result':'Успешно удалено'}, status=200)
