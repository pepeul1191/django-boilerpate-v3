# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        rpta = None
        status = 200
        try:
            rpta = 'hola home'
        except Exception as e:
            rpta = {
                'tipo_mensaje': 'error',
                'mensaje': [
                    'Se ha producido un error en listar los distritos de '
                    + 'la provincia',
                    str(e)
                ],
            }
            status = 500
        return HttpResponse(rpta, status=status,)
    else:
        return HttpResponse('error', status=500)
