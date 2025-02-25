from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('posts/create/', views.create_post, name='create_post'),
]
