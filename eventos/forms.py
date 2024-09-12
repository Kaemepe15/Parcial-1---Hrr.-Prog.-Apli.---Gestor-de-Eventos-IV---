from django import forms
from .models import Evento

#Formulario para el modelo evento

class FormEvento(forms.ModelForm):
    class Datos:
        model= Evento
        fields= ['nombre_org','nombre_event','date_event','descrip_event']

        #Metodo para validar que en el campo de Nombre no se coloque Cancelado
        def BorrarNombre(self):
            nombre= self.cleaned_data.get('nombre_event')
            if 'Cancelado' in nombre:
                raise forms.ValidationError('No puede ingresar en nombre de evento "Cancelado", porfavor ingrese otro nombre para este evento.')
            return nombre