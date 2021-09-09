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
        self.fields['subject'].widget.attrs['placeholder'] = False
        for field in self.fields:
            if field != 'subject':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-box-style'
            self.fields[field].label = False
