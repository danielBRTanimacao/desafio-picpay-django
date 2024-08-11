from ninja import ModelSchema
from .models import Transactions

class TransactionSchema(ModelSchema):
    class Meta:
        model = Transactions
        # exclude = ['id', 'date'] e a merma coisa a diferença que exclui esses e coloca o resto
        fields = ('amount', 'payer', 'payee',)