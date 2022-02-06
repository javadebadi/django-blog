from cProfile import label
from django import forms

class ContactMessageForm(forms.Form):

    phone_number = forms.CharField(
        max_length=12,
        label='Phone number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
            }
        )      
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )      
    )

    name = forms.CharField(
        max_length=128,
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }
        )      
    )

    message = forms.CharField(
        max_length=1500,
        label='Message',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'style': 'height: 12rem;',
                'placeholder': 'Message',
            }
        )
    )