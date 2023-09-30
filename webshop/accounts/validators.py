from django.core.exceptions import ValidationError


def name_validator(name:str) -> None:
    if not name.isalpha():
        raise ValidationError(message='Введите корректное имя')