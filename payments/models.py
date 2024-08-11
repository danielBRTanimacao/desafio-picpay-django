from django.db import models
from decimal import Decimal
from users.models import User

# Create your models here.
class Transactions(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'), editable=False)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    payee = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='payee_user')
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f'Saiu de {self.payer.first_name} para {self.payee.first_name} - R${self.amount}'