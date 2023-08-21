from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('sales/', views.SalesAPIView.as_view(), name='sales'),
    path('sale/<int:pk>/', views.SaleAPIView.as_view(), name='sale'),

    path('products/', views.ProductAPIView.as_view(), name='products'),
    path('brands/', views.BrandAPIView.as_view(), name='brand'),
    path('sellers/', views.SellerAPIView.as_view(), name='seller'),
]