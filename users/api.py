from ninja import Router
from .schemas import UserSchema
# arquivo que sera usado para gerenciar a views

users_router = Router()

# Django-ninja utiliza schema "exemplo type_user_schema"
@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    return {'ok': 'ok'}