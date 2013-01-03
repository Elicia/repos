from principal.models import Receta, Comentario
from django.shortcuts import render_to_response

def lista_bebidas(request):
	receta = Receta.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':receta})