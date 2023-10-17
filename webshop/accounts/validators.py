from django.core.exceptions import ValidationError


def name_validator(name:str) -> None:
    if not name.isalpha():
        raise ValidationError(message='Введите корректное имя')
    
def validate_profile_data(data:dict) -> tuple[bool, str]:
    if not (data['name'] and data['name'].isalpha()):
        return False, f'Поле имя может содержать только буквы и обязательно к заполнению'