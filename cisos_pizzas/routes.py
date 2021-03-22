from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pizzas', views.pizzas),
    path('create_pizza', views.create_pizza),
    path('add_pizza', views.add_pizza),
    path('pizzas/<int:pizza_id>', views.display_pizza),
    path('toppings', views.toppings),
    path('create_topping', views.create_topping),
    path('add_topping', views.add_topping),
    path('toppings/<int:topping_id>', views.display_topping),
]