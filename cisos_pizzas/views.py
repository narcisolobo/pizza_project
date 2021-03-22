from django.shortcuts import render, redirect
from .models import Pizza, Topping

def index(request):
    return redirect('/pizzas')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizzas.html', context)

def create_pizza(request):
    Pizza.objects.create(
        name = request.POST['pizza_name'],
        description = request.POST['pizza_desc'],
    )
    return redirect('/pizzas')

def toppings(request):
    toppings = Topping.objects.all()
    context = {
        'toppings': toppings
    }
    return render(request, 'toppings.html', context)

def create_topping(request):
    Topping.objects.create(
        name = request.POST['topping_name'],
    )
    return redirect('/toppings')

def display_pizza(request, pizza_id):
    correct_pizza = Pizza.objects.get(id=pizza_id)
    toppings_not_on_pizza = Topping.objects.exclude(pizzas__id=correct_pizza.id)
    print(correct_pizza.id)
    context = {
        'pizza': correct_pizza,
        'toppings': toppings_not_on_pizza
    }
    return render(request, 'view_pizza.html', context)

def add_topping(request):
    correct_pizza = Pizza.objects.get(id=request.POST['pizza_id'])
    correct_topping = Topping.objects.get(id=request.POST['topping_id'])
    correct_pizza.toppings.add(correct_topping)
    return redirect(f'pizzas/{correct_pizza.id}')

def add_pizza(request):
    correct_topping = Topping.objects.get(id=request.POST['topping_id'])
    correct_pizza = Pizza.objects.get(id=request.POST['pizza_id'])
    correct_topping.pizzas.add(correct_pizza)
    return redirect(f'toppings/{correct_topping.id}')

def display_topping(request, topping_id):
    correct_topping = Topping.objects.get(id=topping_id)
    non_pizzas = Pizza.objects.exclude(toppings__id=correct_topping.id)
    context = {
        'topping': correct_topping,
        'non_pizzas': non_pizzas
    }
    return render(request, 'view_topping.html', context)