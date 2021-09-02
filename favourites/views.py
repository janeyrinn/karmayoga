from django.shortcuts import render


def view_favourites(request):
    """A view to render the favourites page"""

    return render(request, "favourites/favourites.html")
