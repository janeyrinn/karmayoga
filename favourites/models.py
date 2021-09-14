"""Imports"""
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product


User = get_user_model()


class Favourites(models.Model):
    """A Model to store users favourited items"""

    class Meta:
        verbose_name = 'Favourites'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='FavouritedItem',
                                      related_name='favourited_items')

    def __str__(self):
        return f'({self.user}) Favourites'


@receiver(post_save, sender=User)
def create_favourite_list(sender, instance, created, **kwargs):
    """
    Create the user favourites when a profile is created
    """
    if created:
        Favourites.objects.create(user=instance)
    # Existing users: just save the favourites
        instance.favourites.save()


class FavouritedItem(models.Model):
    """ A Model to allow users to add items to their Favourites"""

    favourites = models.ForeignKey(Favourites, null=False, blank=False,
                                   on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
