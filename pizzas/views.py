from django.shortcuts import render, redirect

from .models import PizzaName
from .forms import PizzaNameForm, ToppingForm, CommentForm

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
    comments = pizzaname.comment_set.order_by('pizzaname_id')
    context = {'pizzaname': pizzaname, 'toppings': toppings, 'comments': comments}
    return render(request, 'pizzas/pizzaname.html', context)

def new_pizzaname(request):
    """Add a new pizza name."""
    if request.method != 'POST':
        form = PizzaNameForm()
    else:
        form = PizzaNameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzanames')

    context = {'form': form}
    return render(request, 'pizzas/new_pizzaname.html', context) 

def new_topping(request, pizzaname_id):
    """Add a new topping for a particular pizza."""
    pizzaname = PizzaName.objects.get(id=pizzaname_id)

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizzaname = pizzaname
            new_topping.save()
            return redirect('pizzas:pizzaname', pizzaname_id=pizzaname_id)

    context = {'pizzaname': pizzaname, 'form': form}
    return render(request, 'pizzas/new_topping.html', context)

def new_comment(request, pizzaname_id):
    pizzaname = PizzaName.objects.get(id=pizzaname_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizzaname = pizzaname
            new_comment.save()
            return redirect('pizzas:pizzaname', pizzaname_id=pizzaname_id)

    context = {'pizzaname': pizzaname, 'form': form}
    return render(request, 'pizzas/new_comment.html', context)