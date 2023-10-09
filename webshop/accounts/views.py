from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from . import models, forms, utils


class ProfileLoginView(LoginView):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'accounts/login.html')
    
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        try:
            profile = models.UserProfile.objects.get(email=request.POST['email'])
            user = profile.user
            login(request, user)
            return redirect(reverse('accounts:homepage'))
        except:
            return JsonResponse(data={'Error':'Invalid data'}, status=400)

class ProfileLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

def homepage(request:HttpRequest):
    return render(request, 'accounts/homepage.html')
    
class RegistrationView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'accounts/registration.html')
    
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        try:
            user = models.User.objects.create(username=request.POST['email'], password=request.POST['password'])
            balance = models.Balance.objects.create(value='0.00')
            profile = models.UserProfile.objects.create(user=user,
                                                        name=request.POST['name'],
                                                        surname=request.POST['surname'],
                                                        age=request.POST['age'],
                                                        phone_number=request.POST['phone_number'],
                                                        email=request.POST['email'],
                                                        password=request.POST['password'],
                                                        balance=balance)
            profile.save()
            login(request, user)
            return redirect(reverse('accounts:homepage'))
        except:
            return JsonResponse(data={'Error':'Invalid data'}, status=400)
        
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
        return render(request, 'accounts/password_reset.html')
        
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        user_profile = get_object_or_404(models.UserProfile, email=request.POST['email'])
        utils.link_token_to_profile(user_profile)
        utils.send_reset_password_link(request, user_profile)
        return HttpResponse('На почту отправленна ссылка. Перейдите по ней, чтобы сменить пароль')
    
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

class ProfileDataView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'accounts/personal_data.html')