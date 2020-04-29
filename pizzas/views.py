from django.shortcuts import render

from .models import PizzaName

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzanames(request):
    """Show all pizza names."""
    pizzanames = PizzaName.objects.order_by('text')
    context = {'pizzanames': pizzanames}
    return render(request, 'pizzas/pizzanames.html', context)

def pizzaname(request, pizzaname_id):
    """Show a single pizza and all its toppings."""
    pizzaname = PizzaName.objects.get(id=pizzaname_id) #pizzaname_id might not be right
    toppings = pizzaname.topping_set.order_by('pizzaname_id')
    context = {'pizzaname': pizzaname, 'toppings': toppings}
    return render(request, 'pizzas/pizzaname.html', context) 