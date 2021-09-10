from django.urls import path
from . import views


""" URL Patterns to open template views"""
urlpatterns = [
    path('', views.index, name='home'),
]
