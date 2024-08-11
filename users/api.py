from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role
from .schemas import TypeUserSchema
from .models import User
from ninja import Router
# arquivo que sera usado para gerenciar a views

users_router = Router()
# Django-ninja utiliza schema "exemplo type_user_schema"

@users_router.post('/', response={200: dict, 400: dict, 500: dict})
def create_user(request, type_user_schema: TypeUserSchema):
    user = User(**type_user_schema.user.dict())
    user.password = make_password(type_user_schema.user.password)
    try:
        user.full_clean()
        user.save()
        assign_role(user, type_user_schema.type_user.type)
    except ValidationError as error:
        return 400, {'errors': error.message_dict}
    except Exception as error:
        return 500, {'errors': 'Erro interno do servidor'}

    return {'user_id': user.id}