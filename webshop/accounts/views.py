from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from . import models


@permission_required()
class UsersAPIView():
    def get(self, request:HttpRequest):
        users_qs = models.UserProfile.objects.all()
        response_data = []
        for user in users_qs:
            pass

    def post(self, request:HttpRequest):
        pass

@permission_required()
class UserAPIView():
    def get(self, request:HttpRequest, pk:int):
        user = models.UserProfile.objects.get(id=pk)
        pass

    def put(self, request:HttpRequest, pk:int):
        pass

    def delete(self, request:HttpRequest, pk:int):
        user = models.UserProfile.objects.get(id=pk)
        user.delete()
        return JsonResponse(data={'result':'Успешно удалено'}, status=200)
    