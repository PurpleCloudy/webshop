from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('sales/', views.SalesAPIView.as_view(), name='sales'),
    path('products/', views.ProductAPIView.as_view(), name='products'),
    path('brand/', views.BrandAPIView.as_view(), name='brand'),
    path('seller/', views.SellerAPIView.as_view(), name='seller'),
]