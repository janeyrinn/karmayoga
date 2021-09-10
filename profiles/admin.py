from django.contrib import admin
from .models import UserProfile

""" Renders the model to the admin backend"""


admin.site.register(UserProfile)
