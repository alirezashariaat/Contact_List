from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'address']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
