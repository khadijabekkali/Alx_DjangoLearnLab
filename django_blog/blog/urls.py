from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User registration
    path('register/', views.register_view, name='register'),

    # Login and logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Profile management
    path('profile/', views.profile_view, name='profile'),
]
