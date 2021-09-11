"""Imports"""
from django.urls import path
from . import views


""" URL Patterns to open template views"""
urlpatterns = [
    path('', views.view_favourites, name='view_favourites'),
    path('add_favourite/<product_id>',
         views.add_favourite, name='add_favourite'),
    path('remove_favourite/<product_id>',
         views.remove_favourite, name='remove_favourite'),
]
