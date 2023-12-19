from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse


class NewLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse("users:user_list")
