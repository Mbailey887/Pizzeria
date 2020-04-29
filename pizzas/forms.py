from django import forms

from .models import PizzaName, Topping

class PizzaNameForm(forms.ModelForm):
    class Meta:
        model = PizzaName
        fields = ['text']
        labels = {'text':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name': 'Topping:'}
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}