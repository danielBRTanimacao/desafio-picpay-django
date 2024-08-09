from ninja import Router
# arquivo que sera usado para gerenciar a views

users_router = Router()

@users_router.post('/', response={200: dict})
def create_user(request):
    return {'ok': 'ok'}