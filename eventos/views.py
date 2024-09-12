from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from djagon.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .models import Organizador
from .models import Evento

#Aquí estaré creando las vistas 
class OrganizadorListView(ListView):
    model= Organizador
    templatename= 'eventos/organizador_list.html'

class OrganizadorCreativeView(CreativeView):
    model= Organizador
    fields= ['nombre_org']
    templatename= 'eventos/organizador_form.html'
    successurl= reverse_lazy('organizador_list')

#Vista protegida para editar eventos
@method_decorator(login_required, name='dispatch')
class EventoUpdateView(UpdateView):
    model= Evento
    fields= ['nombre_event','date_event','descrip_event']
    templatename= 'eventos/evento_form.html'
    successurl= reverse_lazy('evento_list')

