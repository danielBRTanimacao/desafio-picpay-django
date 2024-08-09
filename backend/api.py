from ninja import NinjaAPI 
from users.api import users_router

api = NinjaAPI()
# instancia para a criação de rotas
api.add_router('users/', users_router)