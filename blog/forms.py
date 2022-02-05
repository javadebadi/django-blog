from cProfile import label
from django import forms

class ContactMessageForm(forms.Form):

    phone_number = forms.CharField(
        max_length=12,
        label='Phone number',
    )

    email = forms.EmailField(
        label='Email',
    )

    name = forms.CharField(
        max_length=128,
        label='Name',
    )

    message = forms.CharField(
        max_length=1500,
        label='Message',
    )