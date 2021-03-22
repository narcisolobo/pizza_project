from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cisos_pizzas.routes')),
    path('admin/', admin.site.urls),
]