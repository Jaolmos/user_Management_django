from django import forms

from .models import User

from django.contrib.auth import authenticate

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


class LoginForm(forms.Form):

    username = forms.CharField(
        label = 'Username',
        required = True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username'
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )

    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('User data is not correct')

        return self.cleaned_data 


class UpdatePasswordForm(forms.Form):

    password = forms.CharField(
        label = 'Password',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Current password'
            }
        )

    )

    password2 = forms.CharField(
        label = 'Password',
        required = True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'New password'
            }
        )

    )


class VerificationForm(forms.Form):
    registercode = forms.CharField(required=True)   

    def clean_registercode(self):
        code = self.cleaned_data['registercode']    

        if len(code) == 6:
            active = User.objects.code_validation(
                self.kwargs['pk'],
                code
            )
            if not active:
              raise forms.ValidationError('The code is wrong')   
        else:
            raise forms.ValidationError('The code is wrong')