from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Путь для входа
    path('', views.login_view, name='login'),
    
    # Главная страница
    path('home/', views.home, name='home'),

    # Регистрация
    path('register/', views.register, name='register'),

    # Админка
    path('admin/', admin.site.urls),  # Путь для админки
    
    # Стандартные URL для аутентификации
    path('accounts/', include('django.contrib.auth.urls')),
]
