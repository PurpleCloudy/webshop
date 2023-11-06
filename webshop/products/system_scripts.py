from random import randint
from django.utils.text import slugify
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

class ScriptForm(forms.Form):
    brands = forms.CharField(widget=forms.Textarea)
    sellers = forms.CharField(widget=forms.Textarea)
    products = forms.CharField(widget=forms.Textarea)

def adding(request:HttpRequest):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            for brand in form.cleaned_data['brands'].split(','):
                models.Brand.objects.create(name=brand, slug=slugify(brand), preview='media/path_to_static/no_image_default.jpg', description='asddaksdjaksjdkasjdkajsdkjijihuhiuya', official_name=brand, licence=True)
            for seller in form.cleaned_data['sellers'].split(','):
                models.Seller.objects.create(name=seller, slug=slugify(seller), preview='media/path_to_static/no_image_default.jpg', description='asddaksdjaksjdkasjdkajsdkjijihuhiuya', official_name=seller, licence=True)
            for product in form.cleaned_data['products'].split(','):
                prod = models.Product(category=models.Category.objects.get(id=1), 
                                      brand=models.Brand.objects.get(pk=randint(800, 900)), 
                                      seller=models.Seller.objects.get(pk=randint(1000, 1100)), 
                                      name=product, 
                                      slug=slugify(product), 
                                      preview='path_to_static/no_image_default.jpg', 
                                      description='asddaksdjaksjdkasjdkajsdkjijihuhiuya', 
                                      rating=4, 
                                      price=3, 
                                      amount_sold=200)
                prod.save()
            return HttpResponse(content='Все работает')
    else:
        form = ScriptForm()
        return render(request, 'products/script.html', {'form':form})
