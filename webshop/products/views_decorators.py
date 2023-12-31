import typing
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse

def check_obj_does_not_exist(func:typing.Callable) -> typing.Callable:
    def wrapper(*args, **kwargs) -> JsonResponse:
        try:
            result = func(*args, **kwargs)
            return result
        except ObjectDoesNotExist:
            return JsonResponse(data={'error':'Такого обьекта не существует'}, status=404)
    return wrapper