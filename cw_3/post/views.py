from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_form.html', {'form': form})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def post_create(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=thread_id)
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})
