from ninja import ModelSchema, Schema
from .models import User

#criando um schema intermediario
class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'cpf', 'email', 'password',)


class TypeSchema(Schema):
    type: str


class TypeUserSchema(Schema):
    user: UserSchema
    type_user: TypeSchema 