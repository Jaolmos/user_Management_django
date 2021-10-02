from django.views.generic import CreateView

from django.views.generic.edit import FormView

from .forms import UserRegisterForm


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

