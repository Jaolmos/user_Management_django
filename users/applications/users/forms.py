from django import forms
from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'username',
            'last_name',
            'gender',
        )