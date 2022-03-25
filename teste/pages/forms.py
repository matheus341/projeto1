from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    nascimento = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'nascimento']