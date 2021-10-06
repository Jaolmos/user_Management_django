from  django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User



class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
        )
        return super(UserRegisterForm,self).form_valid(form)

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser,self).form_valid(form)

class LogoutView(View):

    def get(self, requests, *args, **kargs):
        logout(requests)
        return HttpResponseRedirect(
            reverse(
                'users_app:user_login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    #view to update user password
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user_login')
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        userrequest = self.request.user
        user = authenticate(
            username=userrequest.username,
            password=form.cleaned_data['password']
        )
        if user:
            new_password = form.cleaned_data['password2']
            userrequest.set_password(new_password)
            userrequest.save()

        logout(self.request)    
        return super(UpdatePasswordView,self).form_valid(form)
