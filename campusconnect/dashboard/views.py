from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from accounts.models import CustomUser



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_count'] = CustomUser.objects.count()
        context['is_admin'] = (self.request.user.role == CustomUser.Role.ADMIN)
        
        return context

class AdminPanelView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/admin_panel.html'

    def test_func(self):
        user = self.request.user
        return user.role == CustomUser.Role.ADMIN

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "email", "course"]
    template_name = 'dashboard/profile.html'
    success_url = reverse_lazy("dashboard")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "email", "course"]
    template_name = 'dashboard/profile.html'
    success_url = reverse_lazy("dashboard")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        return self.request.user