from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm
from .models import CustomUser
# Create your views here.

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")
    success_message = "Account created successfully! Please log in."


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    fields = ("first_name", "last_name", "email", "course")
    template_name = 'dashboard/profile.html'
    success_url = reverse_lazy("dashboard")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        return self.request.user
