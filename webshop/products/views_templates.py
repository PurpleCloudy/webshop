from datetime import datetime
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from . import models

class Homepage(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        all_sales = models.Sale.objects.order_by('-end_date').all()
        current_sales_row1 = all_sales[:3]
        current_sales_row2 = all_sales[3:6]
        hits = models.Product.objects.order_by('-amount_sold').all()[:30]
        return render(request, 'products/homepage.html', {'categories':models.Category.objects.all(), 'current_sales_row1':current_sales_row1, 'current_sales_row2':current_sales_row2, 'hits':hits})
    
class Category(View):
    @staticmethod
    def get(request:HttpRequest, slug:str):
        category = get_object_or_404(models.Category, slug=slug)
        return render(request, 'products/category_page.html', {'category':category})