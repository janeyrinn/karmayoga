from django.shortcuts import (render, redirect,
                              reverse)
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """A view to render the contact page"""

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'Error, please check the form is valid')

    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
