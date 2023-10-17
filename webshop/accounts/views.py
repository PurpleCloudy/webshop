from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from . import models, forms, utils, validators


class ProfileLoginView(LoginView):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'accounts/login.html')
    
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        try:
            profile = models.UserProfile.objects.get(email=request.POST['email'], password=request.POST['password'])
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
            if request.POST['password_confirm'] == request.POST['password']:
                user = models.User.objects.create(username=request.POST['email'], password=request.POST['password'])
                # balance = models.Balance.objects.create(value='0.00')
                # profile = models.UserProfile.objects.create(user=user,
                #                                             name=request.POST['name'],
                #                                             surname=request.POST['surname'],
                #                                             age=request.POST['age'],
                #                                             phone_number=request.POST['phone_number'],
                #                                             email=request.POST['email'],
                #                                             password=request.POST['password'],
                #                                             balance=balance)
                # profile.save()
                login(request, user)
                return redirect(reverse('accounts:homepage'))
            else:
                raise Exception
        except:
            return JsonResponse(data={'Error':'Invalid data'}, status=400)
        
class UpdateProfileView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        return render(request, 'accounts/update_profile.html')

    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        user = request.user
        if user.is_authenticated:
            profile_data_is_valid = validators.validate_profile_data(request.POST)
            if not profile_data_is_valid[0]:
                return JsonResponse(data={'error':f'{profile_data_is_valid[1]}'}, status=400)
            profile = user.profile
            utils.update_profile(profile, request.POST)
            return redirect(reverse('accounts:homepage'))
        return redirect(reverse('accounts:login'))
        
class ProfilePasswordResetView(View):
    @staticmethod
    def get(request:HttpRequest) -> HttpResponse:
        user = request.user
        if user.is_authenticated:
            utils.link_token_to_profile(user.profile)
            utils.send_reset_password_link(request, user.profile)
            return render(request, 'accounts/send_link.html')
        return render(request, 'accounts/password_reset.html')
        
    @staticmethod
    def post(request:HttpRequest) -> HttpResponse:
        user_profile = get_object_or_404(models.UserProfile, email=request.POST['email'])
        utils.link_token_to_profile(user_profile)
        utils.send_reset_password_link(request, user_profile)
        return render(request, 'accounts/send_link.html')
    
class ProfilePasswordResetDoneView(View):
    @staticmethod
    def get(request:HttpRequest, reset_token:str) -> HttpResponse:
        return render(request, 'accounts/password_reset_done.html', {'reset_token':reset_token})
    
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