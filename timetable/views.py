from django.shortcuts import render


def about(request):
    """ A view to return the timetable page """

    return render(request, 'templates/timetable.html')
