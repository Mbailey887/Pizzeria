import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import PizzaName

pizzas = PizzaName.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

t = PizzaName.objects.get(id=2)
print(t.text)

names = t.topping_set.all()

for name in names:
    print(name)