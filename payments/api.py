from ninja import Router

payments_router = Router()

@payments_router.post('/', response={200: dict})
def transactions(request):

    return {'ok': 'ok'}