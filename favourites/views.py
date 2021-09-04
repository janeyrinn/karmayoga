from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Favourites
from products.models import Product


@login_required
def view_favourites(request):
    """A view to display a users favourites"""

    favourites = None
    try:
        favourites = Favourites.objects.get(user=request.user)
    except Favourites.DoesNotExist:
        pass

        context = {
            'favourites': favourites,
        }

    return render(request, 'favourites/favourites.html', context)


@login_required
def add_favourite(request, product_id):
    """Adds a product to the users 'Favourites' """

    product = get_object_or_404(Product, pk=product_id)
    # Creates the users 'favourites' container if one doesn't exist
    favourites, _ = Favourites.objects.get_or_create(user=request.user)

    if product in favourites:
        favourites.products.remove(product)
        messages.success(request, 'Product removed from favourites')
    else:
        # Adds the selected product to the favourites
        favourites.products.add(product)
        messages.success(request, f'{product.name}\
            was added to your saved items')

    return redirect(request.META.get('HTTP_REFERER'))
