from django import forms
from .models import Signup

class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": 'email',
        'id': "email",
        "name": "email",
        "placeholder": "Type your email address",
        'label': ''
    }), label='')
    class Meta:
        model = Signup
        fields =('email',)