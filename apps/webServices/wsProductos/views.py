# Create your views here.
from django.http import HttpResponse
from demojuan.apps.ventas.models import Producto
# integrando la serializacion de los objetos
from django.core import serializers


def wsProductos_view(request):
	data = serializers.serialize("json",Producto.objects.filter(status=True))
	return  HttpResponse(data,mimetype='application/json')

def wsProductosId_view(request,id):
	data = serializers.serialize("json",Producto.objects.get(pk="%s"%id))
	return HttpResponse(data,mimetype='application/json')