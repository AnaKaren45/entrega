from django.conf.urls import patterns, url
#from computadora.apps.armadopc import views
from computadora.apps.cliente.views import *
urlpatterns = patterns('',
	
	
	url(r'^base/page/(?P<pagin>.*)/$',placa2),	
	url(r'^placas/(?P<id_placa>.*)/$',verplaca),
	url(r'^compo/page/(?P<pagin>.*)/$',componente2),
	url(r'^vercomponente/(?P<id_comp>.*)/$',vercomponent),
	#para carrito placa####
	url(r'^cliente/cargar/carrito/(?P<id>.*)/$',cargar_carrito),
	url(r'^cliente/carrito/add/(?P<id>)/$',carrito_add),
	url(r'^cliente/mostrar/carrito/$',carrito_mostrar),
	url(r'^confirmar/compra/$',confirmar_compra),
	url(r'^reserva/$',reserva),	

	#para carrito componenrte
	url(r'^cliente/cargar/carrito1/(?P<id>.*)/$',cargar_carrito1),	


	
    
   
    
    #url(r'^carrito/eliminar/(?P<id>)/$',eliminar_de_carrito),

    #url(r'^cliente/(?P<id>\d+)/$',listar_producto),
    #url(r'^confirmar/compra/$',confirmar_compra),

)



