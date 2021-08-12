from django import forms
from .models import Tarea

class TareasForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['tarea']