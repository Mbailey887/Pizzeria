from django.contrib import admin

# Register your models here.
from .models import PizzaName
from .models import Topping
from .models import Comment

admin.site.register(PizzaName)
admin.site.register(Topping)
admin.site.register(Comment)