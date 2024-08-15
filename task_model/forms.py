from django import forms
from .models import ModelF

class TaskForm(forms.ModelForm):
    class Meta:
        model = ModelF
        fields = '__all__'