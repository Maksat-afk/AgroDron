from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts_list')
    return render(request, 'posts/login.html')  # ✅ Правильный путь

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'posts/register.html', {'form': form})  # ✅ Правильный путь

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})  # ✅ Правильный путь

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})  # ❌ Было: 'my_posts.html' → ✅ Исправлено: 'posts/my_posts.html'

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})  # ✅ Правильный путь

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})  # ❌ Было: 'create_post.html' → ✅ Исправлено: 'posts/create_post.html'

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('posts_list')
    return HttpResponseForbidden()
