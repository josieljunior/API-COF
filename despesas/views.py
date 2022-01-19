from django.http import JsonResponse

def despesas(request):
    if request.method == 'GET':
        despesas = {
            'id':1,
            'descricao:': 'mercado',
            'valor': 100,
            'data': '10/01/22'
        }
        return JsonResponse(despesas)