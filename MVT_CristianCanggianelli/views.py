from django.http import HttpResponse
from django.template import loader

def inicio(request):
    data = {'nombre':'Cristian','apellido':'Canggianelli'}
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render(data)
    
    return HttpResponse(documento)

