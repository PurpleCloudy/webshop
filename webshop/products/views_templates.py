from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpRequest, HttpResponse
from . import models, serializers, paginators


class Homepage(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        all_sales = models.Sale.objects.order_by('-end_date').all()[:6]
        hits = models.Product.objects.order_by('-amount_sold').all()[:300]
        hits_data = paginators.products_pagination(request=request, pagination_data=hits, default_size=6)
        products = models.Product.objects.order_by('-amount_sold')[hits_data['start_index']:hits_data['end_index']]
        response_data = serializers.serialize_product_pagination(products)
        return render(request, 'products/homepage.html', {
            'categories': models.Category.objects.all(),
            'allsales': all_sales,
            'hits': response_data,
            'page': hits_data['page'],
            'pages_number': hits_data['pages_number'],
        })


class Category(View):
    @staticmethod
    def get(request: HttpRequest, slug: str):
        category = get_object_or_404(models.Category, slug=slug)
        subcategories = models.Category.objects.filter(parent=category)
        all_sales = models.Sale.objects.order_by('-end_date').all()[:6]
        hits = models.Product.objects.order_by('-amount_sold').filter(category=category)
        hits_data = paginators.products_pagination(request=request, pagination_data=hits, default_size=6)
        products = models.Product.objects.order_by('-amount_sold')[hits_data['start_index']:hits_data['end_index']]
        response_data = serializers.serialize_product_pagination(products)
        return render(request, 'products/category_products.html', {
            'parent_category': category,
            'categories': subcategories,
            'allsales': all_sales,
            'hits': response_data,
            'page': hits_data['page'],
            'pages_number': hits_data['pages_number'],
        })


class HitsCatalog(View):
    @staticmethod
    def get(request: HttpRequest):
        hits_data = paginators.products_pagination(request=request, pagination_data=models.Product.objects.all(), default_size=35)
        products = (models.Product.objects.order_by('-amount_sold')[hits_data['start_index']:hits_data['end_index']])
        response_data = serializers.serialize_product_pagination(products)
        return render(
            request, 'products/hits_catalog.html',
            {
                'hits': response_data,
                'pages_number': hits_data['pages_number'],
                'page': hits_data['page'],
            }
        )

        # return JsonResponse(data={'hits': response_data}, status=200)


class ProductCardView(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        product = models.Product.objects.get(id=pk)
        return render(request, 'products/product_card.html', serializers.serialize_product_obj(product))

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        user = request.user
        if user.is_authenticated():
            product = models.Product.objects.get(id=pk)
            models.Feedback.objects.create(
                author=user.profile,
                product=product,
                paragraph=request.POST['paragraph'],
                main_content=request.POST['main_content'],
                rating=request.POST['rating'],
            )
            return render(request, 'products/product_card.html', serializers.serialize_product_obj(product))
        return redirect(reverse('login'))
