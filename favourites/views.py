from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Favourites


@login_required
def view_favourites(request):
    """A view to display a users favourites"""

    favourites = Favourites.objects.get(user=request.user)

    template = 'favourites/favourites.html'
    context = {
            'favourites': favourites,
        }

    return render(request, template, context)


@login_required
def add_favourite(request, product_id):
    """Adds a product to the users 'Favourites' """

    product = get_object_or_404(Product, pk=product_id)

    # Creates the users 'favourites' container if one doesn't exist
    favourites, _ = Favourites.objects.get_or_create(user=request.user)

    # Adds the selected product to the favourites
    favourites.products.add(product)
    messages.success(request, f'{product.name}\
        added to favourites')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_favourite(request, product_id):
    """Removes a product to the users 'Favourites' """

    product = get_object_or_404(Product, pk=product_id)
    favourites = Favourites.objects.get(user=request.user)

    # Removes the selected product from favourites
    favourites.products.remove(product)
    messages.info(request, f'{product.name}\
        removed from favourites')

    return redirect(request.META.get('HTTP_REFERER'))
