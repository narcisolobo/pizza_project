from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Topping(models.Model):
    name = models.CharField(max_length=45)
    pizzas = models.ManyToManyField(Pizza, related_name='toppings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)