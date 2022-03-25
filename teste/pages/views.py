from django.views.generic import  TemplateView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy
class HomePageView(TemplateView):
    template_name = "home.html"

class UsuarioCreate(CreateView):
   success_url = reverse_lazy("account_login")
   template_name = "account/signup.html"
   form_class = UserForm
