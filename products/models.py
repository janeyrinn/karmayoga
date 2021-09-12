"""
Imports
"""
from django.db import models


class Category(models.Model):
    """ Creates Category model"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100,
                                     default='blank', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Retrieves friendly name"""
        return self.friendly_name


class Product(models.Model):
    """ Creates Product Model """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, null=True,
                                decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
