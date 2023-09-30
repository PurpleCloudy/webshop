from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from . import models, forms, utils


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
            return JsonResponse(data={'error':'Не валидные данные'}, status=400)
        return redirect(reverse('accounts:login'))
        
class ProfilePasswordResetView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        user = request.user
        if user.is_authenticated:
            utils.link_token_to_profile(user.profile)
            utils.send_reset_password_link(request, user.profile)
            return HttpResponse('На почту отправленна ссылка. Перейдите по ней, чтобы сменить пароль')
        form = forms.PasswordResetForm()
        return render(request, 'accounts/password_reset.html', {'form':form})
        
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user_profile = get_object_or_404(models.UserProfile, email=form.cleaned_data['email'])
            utils.link_token_to_profile(user_profile)
            utils.send_reset_password_link(request, user_profile)
            return HttpResponse('На почту отправленна ссылка. Перейдите по ней, чтобы сменить пароль')
        return JsonResponse(data={'error':'Невалидные данные'})
    
class ProfilePasswordResetDoneView(View):
    @staticmethod
    def get(request:HttpRequest, reset_token:str) -> HttpResponse:
        form = forms.PasswordResetDoneForm()
        return render(request, 'accounts/password_reset_done.html', {'form':form})
    
    @staticmethod
    def post(request:HttpRequest, reset_token:str) -> HttpResponse:
        profile = models.UserProfile.objects.get(reset_token=reset_token)
        form = forms.PasswordResetDoneForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            utils.update_password_and_login(request, profile, form.cleaned_data['password'])
            return redirect(reverse('accounts:homepage'))
        return JsonResponse(data={'error':'Невалидные данные'}, status=400)
