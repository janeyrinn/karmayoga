from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favourites, name='view_favourites'),
    path('add_favourite/<product_id>',
         views.add_favourite, name='add_favourite'),
]
