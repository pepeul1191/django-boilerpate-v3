# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def index_rest(request):
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

def index_view(request):
    locals = {}
    return render(request, 'home/index.html', locals)
