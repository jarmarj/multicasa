from django import forms
from casas.models import ClienteCasa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteCasa 
        fields = [
            'correo',
            'telefono',
            'casa'
        ]
    