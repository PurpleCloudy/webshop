from django.contrib import admin
from django.urls import path
from . import views_api, views_templates, system_scripts

app_name = 'products'

urlpatterns = [
    path('homepage/', views_templates.Homepage.as_view(), name='homepage'),

    path('category/<slug:slug>', views_templates.Category.as_view(), name='category'),

    path('hits/catalog/', views_templates.Pagination.as_view(), name='catalog'),

    path('sales/', views_api.SalesAPIView.as_view(), name='sales'),
    path('sale/<int:pk>/', views_api.SaleAPIView.as_view(), name='sale'),

    path('products/', views_api.ProductsAPIView.as_view(), name='products'),
    path('product/<int:pk>/', views_api.ProductAPIView.as_view(), name='product'),
    
    path('brands/', views_api.BrandsAPIView.as_view(), name='brands'),
    path('brand/<int:pk>/', views_api.BrandAPIView.as_view(), name='brand'),

    path('sellers/', views_api.SellersAPIView.as_view(), name='seller'),
    path('seller/<int:pk>/', views_api.SellerAPIView.as_view(), name='seller'),

    path('script/', system_scripts.adding, name='script'),
]