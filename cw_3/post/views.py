from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def thread_edit(request, id):
    # Логика редактирования темы
    pass  

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    # Логика редактирования сообщения
    pass  

