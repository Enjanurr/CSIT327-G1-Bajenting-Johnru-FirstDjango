from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('feedback/', views.feedback_view, name='feedback'),
    path(
        'feedback/success/',
        login_required(TemplateView.as_view(template_name='accounts/feedback_success.html')),
        name='feedback-success',
    ),
]