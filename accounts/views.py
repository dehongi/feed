from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "signup.html"  # Specify your template name
    success_url = reverse_lazy("login")  # Redirect to login page after signup
