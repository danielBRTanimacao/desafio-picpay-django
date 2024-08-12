from backend.settings import AUTHORIZE_TRANSFER_ENDPOINT
from django.db import transaction as django_transaction
from rolepermissions.checkers import has_permission
from django.shortcuts import get_object_or_404
from .schemas import TransactionSchema
from .models import Transactions
from users.models import User
from ninja import Router
import requests

payments_router = Router()

@payments_router.post('/', response={200: dict, 400: dict, 403: dict})
def transactions(request, data_transaction: TransactionSchema):
    payer = get_object_or_404(User, id=data_transaction.payer)
    payee = get_object_or_404(User, id=data_transaction.payee)

    if payer.amount < data_transaction.amount:
        return {400: {'error': "Saldo insuficiente para a transação!"}}

    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': "Você não tem autorização para fazer esta transação"}
    
    if not has_permission(payee, 'receive_transfer'):
        return 403, {'error': "O usuario não tem autorização para receber transferencia"}
    
    with django_transaction.atomic():
        payer.pay(data_transaction.amount)
        payee.receive(data_transaction.amount)

        transct = Transactions(
            amount= data_transaction.amount,
            payer_id= data_transaction.payer,
            payee_id= data_transaction.payee,
        )
        payer.save()
        payee.save()
        transct.save()

        response = requests.get(AUTHORIZE_TRANSFER_ENDPOINT).json()
        if response.get('status') != 'authorized': raise Exception()

    return 200, {'data_transaction': 1}