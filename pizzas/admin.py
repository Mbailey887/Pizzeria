from django.contrib import admin

# Register your models here.
from .models import PizzaName
from .models import Topping

admin.site.register(PizzaName)
admin.site.register(Topping)