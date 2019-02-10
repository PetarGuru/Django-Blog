from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:post_id>', views.detail, name='detail'),
]