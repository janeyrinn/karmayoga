from django.db import models
from products.models import Product
from django.contrib.auth.models import User


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


class FavouritedItem(models.Model):
    """ A Model to allow users to add items to their Favourites"""

    favourites = models.ForeignKey(Favourites, null=False, blank=False,
                                   on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
