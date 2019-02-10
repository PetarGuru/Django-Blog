
from django.urls import path

from .views import email_view, success_view

urlpatterns = [
    path('email/', email_view, name='email'),
    path('success/', success_view, name='success'),
]

