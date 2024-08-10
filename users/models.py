from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        return super(User, self).save(*args, **kwargs)
    
    def pay(self, value: Decimal):
        assert isinstance(value, Decimal), 'O value deve ser Decimal!'
        self.amount -= value
        # fazendo atomicidade para confirmar envio em toda base SQL

    def receive(self, value: Decimal):
        assert isinstance(value, Decimal), 'O value deve ser Decimal!'
        self.amount += value