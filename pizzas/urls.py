"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizza names
    path('pizzanames/', views.pizzanames, name='pizzanames'),
    # Detail page for a single pizza
    path('pizzanames/<int:pizzaname_id>/', views.pizzaname, name='pizzaname'),
    # page for adding a new pizza
    path('new_pizzaname', views.new_pizzaname, name='new_pizzaname'),
    # Page for adding new toppings
    path('new_topping/<int:pizzaname_id>/', views.new_topping, name='new_topping'),
]