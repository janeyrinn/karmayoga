from django.shortcuts import render


def view_timetable(request):
    """ A view to return the timetable template """

    return render(request, 'timetable/timetable.html')
