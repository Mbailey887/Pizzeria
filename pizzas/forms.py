from django import forms

from .models import PizzaName

class PizzaNameForm(forms.ModelForm):
    class Meta:
        model = PizzaName
        fields = ['text']
        labels = {'text':''}