from django.contrib import admin
from .models import Favourites, FavouritedItem

""" Renders the two models to the admin backend"""

admin.site.register(Favourites)
admin.site.register(FavouritedItem)
