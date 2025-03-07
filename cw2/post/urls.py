from django.contrib import admin
from django.urls import path
from .views import index  # Импортируем index из views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Главная страница
]
