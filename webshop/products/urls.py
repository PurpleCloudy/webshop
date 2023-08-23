from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('sales/', views.SalesAPIView.as_view(), name='sales'),
    path('sale/<int:pk>/', views.SaleAPIView.as_view(), name='sale'),

    path('products/', views.ProductsAPIView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductAPIView.as_view(), name='product'),
    
    path('brands/', views.BrandsAPIView.as_view(), name='brands'),
    path('brand/<int:pk>/', views.BrandAPIView.as_view(), name='brand'),

    path('sellers/', views.SellersAPIView.as_view(), name='seller'),
    path('seller/<int:pk>/', views.SellerAPIView.as_view(), name='seller'),
]