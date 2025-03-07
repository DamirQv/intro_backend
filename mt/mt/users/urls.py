from django.urls import path
from .views import get_users, create_user, get_user

urlpatterns = [
    path("", get_users),
    path("/int:id", get_user),
    path("/create", create_user),
]
