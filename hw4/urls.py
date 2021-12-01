from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('completed/<str:id>', views.completed, name="completed"),
    path('add/', views.add, name="add"),

]
