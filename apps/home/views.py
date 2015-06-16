from django.shortcuts import render_to_response
from django.template import RequestContext
from demojuan.apps.ventas.models import Producto
from demojuan.apps.home.forms import contactFrom
from django.core.mail import EmailMultiAlternatives

def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	mensaje = "este es un mensaje de la visata"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx, context_instance=RequestContext(request))

def productos_view(request):
	produc = Producto.objects.filter(status=True)
	ctx = {'productos':produc}
	return render_to_response('home/productos.html',ctx, context_instance=RequestContext(request))


def contacto_view(request):
	info_enviado = False
	email 	= ""
	titulo 	= ""
	texto 	= ""
	if request.method == "POST":
		formulario = contactFrom(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = 	formulario.cleaned_data['Email']
			titulo = 	formulario.cleaned_data['Titulo']
			texto = 	formulario.cleaned_data['Texto']
			# configuracion enviondo mensaje via gmail
			to_admin = 'juan.carrasco@clockwise.cl'
			html_content = "Informacion recibida [%s]<br><br><br>***Mensaje***<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto', html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = contactFrom()
	ctx = {'form':formulario, 'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx, context_instance=RequestContext(request))