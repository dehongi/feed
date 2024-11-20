from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'  # Specify your template name
    success_url = reverse_lazy('login')  # Redirect to login page after signup

    def form_valid(self, form):
        # Save the new user
        user = form.save()
        # Log the user in after successful signup
        login(self.request, user)
        return redirect(self.success_url)