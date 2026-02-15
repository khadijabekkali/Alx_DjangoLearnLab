from django.urls import path
from . import views

urlpatterns = [
    # Blog post CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Authentication URLs (already created)
    path('register/', views.register_view, name='register'),
    path('login/', views.auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
