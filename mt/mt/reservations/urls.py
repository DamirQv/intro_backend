from django.urls import path
from .views import get_reservations, create_reservation

urlpatterns = [
    path("<int:id>", get_reservations),
    path("/create", create_reservation),
]