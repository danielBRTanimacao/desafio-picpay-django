from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .schemas import UserSchema
from .models import User
from ninja import Router
# arquivo que sera usado para gerenciar a views

users_router = Router()
# Django-ninja utiliza schema "exemplo type_user_schema"

@users_router.post('/', response={200: dict, 400: dict, 500: dict})
def create_user(request, user: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    try:
        user.full_clean()
        user.save()
    except ValidationError as error:
        return 400, {'errors': error.message_dict}
    except Exception as error:
        return 500, {'errors': 'Erro interno do servidor'}

    return {'ok': 'ok'}