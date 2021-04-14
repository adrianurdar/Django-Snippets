from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, CustomUser


class UserRegisterForm(UserCreationForm):
    """
    Register form for new users.
    """

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume de familie',
            'email': 'Email',
            'password1': 'Parola',
            'password2': 'Confirmarea parolei',
        }


class UserUpdateForm(forms.ModelForm):
    """
    Update info form for existing users.
    """

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume de familie',
            'email': 'Email',
        }


class ProfileUpdateForm(forms.ModelForm):
    """
    Update profile image form for existing users.
    """

    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': 'Imagine',
        }
