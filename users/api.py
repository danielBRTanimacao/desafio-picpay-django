from django.contrib.auth.hashers import make_password
from .schemas import UserSchema
from .models import User
from ninja import Router
# arquivo que sera usado para gerenciar a views

users_router = Router()
# Django-ninja utiliza schema "exemplo type_user_schema"

@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    user.save()
    return {'ok': 'ok'}