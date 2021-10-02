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

        def clean_password2(self):
            if self.cleaned_data['password1'] != self.cleaned_date['password2']:
                self.add_error('password2', 'Passwords do not match')

        