from django import forms

class ContactMessageForm(forms.Form):

    phone_number = forms.CharField(
        max_length=12,
    )

    email = forms.EmailField()

    name = forms.CharField(
        max_length=128,
    )

    message = forms.CharField(
        max_length=1500,
    )