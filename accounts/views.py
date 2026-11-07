from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileUpdateForm
from .models import CustomUser


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "Account created successfully! You can now log in."


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')
    success_message = "Profile updated successfully."

    def get_object(self, queryset=None):
        return self.request.user