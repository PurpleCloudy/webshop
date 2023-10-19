from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import models

class Homepage(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'products/homepage.html', {'categories':models.Category.objects.all()})