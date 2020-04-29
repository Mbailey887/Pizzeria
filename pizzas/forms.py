from django import forms

from .models import PizzaName, Topping, Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': 'Comment:'}
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}