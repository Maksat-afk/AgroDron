from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Функция для входа в систему
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после успешного входа
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Главная страница
def home(request):
    return render(request, 'home.html')

# Другие функции, например, для регистрации
def register(request):
    return render(request, 'register.html')
