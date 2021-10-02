from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label = 'Password',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Password',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repeat password'
            }
        )

    )
    
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