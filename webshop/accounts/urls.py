from django import urls
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.ProfileLoginView.as_view(), name='login'),
    path('logout/', views.ProfileLogoutView.as_view(), name='logout'),
    # path('logout/', views.logout_view, name='logout'),
    # path('login/', views.login, name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('homepage/', views.homepage, name='homepage'),
]