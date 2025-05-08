from django.urls import path, include
from rest_framework_nested import routers
from . import views  # Импортируем views

from .views import PostViewSet, CommentViewSet, register, login_view

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    # Регистрируем API-роуты
    path('api/', include(router.urls)),
    path('api/', include(posts_router.urls)),

    # Статические маршруты
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
