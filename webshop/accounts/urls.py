from django import urls
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.ProfileLoginView.as_view(), name='login'),
    path('logout/', views.ProfileLogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('homepage/', views.homepage, name='homepage'),
    path('password_reset/', views.ProfilePasswordResetView.as_view(), name='password_reset'),
    path('password_reset/<str:reset_token>/', views.ProfilePasswordResetDoneView.as_view(), name='password_reset_done'),
    path('personal_data/', views.ProfileDataView.as_view(), name='personal_data')
]