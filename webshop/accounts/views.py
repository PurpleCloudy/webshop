from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, Pa
from . import models, forms


class ProfileLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('accounts:homepage')
    redirect_authenticated_user = reverse_lazy('accounts:homepage')

class ProfileLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

# def login_view(request:HttpRequest):
#     if request.method == 'POST':
#         form = forms.AuthenticationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['email'], form.cleaned_data['password'])
#             user = User.objects.get(email=form.cleaned_data['email'])
#             if user:
#                 user = authenticate(request, username=user.username, password=user.password)
#                 if user:
#                     login(request, user)
#                     return render(request, 'accounts/homepage.html')
#             else:
#                 return JsonResponse(data={'error':'Неверный логин или пароль'}, status=400)
#     else:
#         form = forms.AuthenticationForm()
#         return render(request, 'accounts/login.html', {'form':form})
    
def logout_view(request:HttpRequest):
    logout(request)
    return render(request, 'accounts/homepage.html')

def homepage(request:HttpRequest):
    return render(request, 'accounts/homepage.html')

# def registration_view(request:HttpRequest):
#     if request.method == 'POST':
#         form = forms.RegistrationForm(request.POST)
#         if form.is_valid():
#             user = models.User.objects.create(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
#             balance = models.Balance.objects.create(value='0.00')
#             profile = models.UserProfile.objects.create(user=user, **form.cleaned_data, balance=balance)
#             profile.save()
#             login(request, user)
#             return redirect(reverse('accounts:homepage'))
#         else:
#             return JsonResponse(data={'error':'Неверные данные'}, status=400)
#     else:
#         form = forms.RegistrationForm()
#         return render(request, 'accounts/registration.html', {'form':form})
    
class RegistrationView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        form = forms.RegistrationForm()
        return render(request, 'accounts/registration.html', {'form':form})
    
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = models.User.objects.create(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            balance = models.Balance.objects.create(value='0.00')
            profile = models.UserProfile.objects.create(user=user, **form.cleaned_data, balance=balance)
            profile.save()
            login(request, user)
            return redirect(reverse('accounts:homepage'))
        else:
            return JsonResponse(data={'error':'Неверные данные'}, status=400)
        
class UpdateProfileView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        form = forms.ChangeDetailForm()
        return render(request, 'accounts/update_profile.html', {'form':form})

    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        user = request.user
        if user.is_authenticated:
            form = forms.ChangeDetailForm(request.POST)
            if form.is_valid():
                models.UserProfile.objects.filter(pk=user.id).update(**form.cleaned_data)
                return redirect(reverse('accounts:homepage'))
        else:
            return redirect(reverse('accounts:login'))
        

