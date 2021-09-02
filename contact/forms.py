from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for Contact model """
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated
        labels, sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
