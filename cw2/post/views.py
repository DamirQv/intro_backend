from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Message
from .forms import MessageForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, это главная страница!")


# Получить все сообщения
def get_messages(request):
    messages = Message.objects.all().values()
    return JsonResponse(list(messages), safe=False)

# Получить сообщение по ID
def get_message(request, id):
    message = get_object_or_404(Message, id=id)
    return JsonResponse({"title": message.title, "description": message.description, "author": message.author})

# Создать сообщение
def create_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages_page')  # Перенаправление на страницу со списком сообщений
    else:
        form = MessageForm()
    return render(request, 'post/create_message.html', {'form': form})

# Удалить сообщение
def delete_message(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    return redirect('messages_page')  # Перенаправление на страницу со списком сообщений

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Отображаем шаблон index.html

