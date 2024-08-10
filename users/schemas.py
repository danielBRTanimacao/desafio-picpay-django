from ninja import ModelSchema, Schema
from .models import User

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'cpf', 'email', 'password',)