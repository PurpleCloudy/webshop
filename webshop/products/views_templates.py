from math import ceil
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from . import models


class Homepage(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        all_sales = models.Sale.objects.order_by('-end_date').all()[:6]
        hits = models.Product.objects.order_by('-amount_sold').all()[:300]
        return render(request, 'products/homepage.html', {
                                                                    'categories': models.Category.objects.all(),
                                                                    'allsales': all_sales,
                                                                    'hits': hits
                                                                        })


class Category(View):
    @staticmethod
    def get(request: HttpRequest, slug: str):
        category = get_object_or_404(models.Category, slug=slug)
        subcategories = models.Category.objects.filter(parent=category)
        all_sales = models.Sale.objects.order_by('-end_date').all()[:6]
        hits = models.Product.objects.order_by('-amount_sold').filter(category=category)[:30]
        return render(request, 'products/homepage.html', {
                                                                                'parent_category': category,
                                                                                'categories': subcategories,
                                                                                'allsales': all_sales,
                                                                                'hits': hits
                                                                                    })


class Pagination(View):
    @staticmethod
    def get(request: HttpRequest):
        try:
            page = int(request.GET['page'])
            page_size = int(request.GET['page_size'])
        except (ValueError, Exception):
            page = 1
            page_size = 35
        start_index = (page-1)*page_size
        end_index = page*page_size
        print(start_index, end_index)
        hits = models.Product.objects.order_by('-amount_sold')[start_index:end_index]
        pages_number = ceil(len(models.Product.objects.all())/page_size)
        response_data = []
        for hit in hits:
            name = str(hit.name[:30]+'...').replace("'", "")
            response_data.append(
                {
                    'id': hit.pk,
                    'category': hit.category,
                    'brand': hit.brand,
                    'seller': hit.seller,
                    'sale': hit.sale,
                    'name': name,
                    'slug': hit.slug,
                    'description': hit.description,
                    'rating': hit.rating,
                    'price': hit.price,
                    'preview':hit.preview.url,
                })
        return render(request, 'products/hits_catalog.html', {'hits':response_data, 
                                                              'pages_number':pages_number, 
                                                              'pages_number_prev1':pages_number-1,
                                                              'pages_number_prev2':pages_number-2,
                                                              'pages_number_prew3':pages_number-3,
                                                              'page':page,
                                                              'page_prew1':page-1,
                                                              'page_post1':page+1,
                                                              })

        # return JsonResponse(data={'hits': response_data}, status=200)

    @staticmethod
    def post(request: HttpRequest):
        print(request.POST)
        return HttpResponse(status=200)
