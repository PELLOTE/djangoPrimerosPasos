from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demojuan.apps.webServices.wsProductos.views',
	url(r'^ws/Productos/$','wsProductos_view', name='ws_productos_url'),
	url(r'^ws/Producto/(?P<id>\d+)/$','wsProductosId_view'),
	#url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
	
)