from django.shortcuts import render,render_to_response
# Create your views here.
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
# importando el paginador
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from computadora.apps.cliente.forms import *
from computadora.apps.armadopc.models import *
import json

import hashlib
import datetime

###############   Placa    ##################		
def placa2(request,pagin):
	lista_placa =Placa.objects.all()
	paginator=Paginator(lista_placa,3)#cuantos productos quieres mostrar
	try:
		page = int(pagin)
	except:
		page = 1
	try:
		placa=paginator.page(page)
	except (EmptyPage,InvalidPage):
		placa=paginator.page(paginator.num_pages)
	return render_to_response("cliente/placados.html",{"placa":placa},context_instance=RequestContext(request))
def verplaca(request,id_placa):
	placa=Placa.objects.get(id=id_placa)
	return render_to_response("cliente/verplaca.html",{"placa":placa},context_instance=RequestContext(request))
############## COMPONENTE #########################
def componente2(request,pagin):
	lista_form = Componente.objects.all()
	paginator=Paginator(lista_form,3)#cuantos productos quieres mostrar
	try:
		page = int(pagin)
	except:
		page = 1
	try:
		placa=paginator.page(page)
	except (EmptyPage,InvalidPage):
		placa=paginator.page(paginator.num_pages)
	return render_to_response("cliente/componente2.html",{"componente":placa},context_instance=RequestContext(request))

def vercomponent(request,id_comp):
	comp=Componente.objects.get(id=id_comp)
	#cats=comp.categorias.all() #Obteniendo la categoria del componente
	ctx={"componente":comp}
	return render_to_response("cliente/verproducto.html",ctx,context_instance=RequestContext(request))


############para carrito placas#############3
def cargar_carrito(request,id):
    pro=Placa.objects.get(id=int(id))
    fcarr=fcarrito()
    return render_to_response("cliente/fcarrito.html",{'fcarr':fcarr,'pro':pro},context_instance=RequestContext(request))
def carrito_add(request,id):
    if request.method=="POST":
        cant=request.POST['cantidad']
        if int(cant)>0:
            pro=Placa.objects.get(id=int(id))
            carr=Carrito.objects.create(id_sesion="1212",estado=False,placa=pro,cantidad=int(cant))

    return HttpResponseRedirect("/cliente/mostrar/carrito/")
def confirmar_compra(request):
    if request.user.is_authenticated():
        carr=Carrito.objects.filter()
        return render_to_response("cliente/confirmar_compra.html",{'carr':carr},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/usuario/ingresar/")

def carrito_mostrar(request):
    if not "contador" in request.session:
        request.session['contador'] = 0
    return HttpResponse(request.session['contador'])

#################para el carrito componente#############
def cargar_carrito1(request,id):
    pro=Componente.objects.get(id=int(id))
    fcarr=fcarrito()
    return render_to_response("cliente/fcarrito1.html",{'fcarr':fcarr,'pro':pro},context_instance=RequestContext(request))

def reserva(request):
 
    return render_to_response("cliente/reserva.html",context_instance=RequestContext(request))
