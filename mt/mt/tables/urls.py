from django.urls import path
from .views import get_tables, create_table

urlpatterns = [
    path("", get_tables),
    path("/create", create_table),
]