from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register_view, name='register'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Profile management (view & edit)
    path('profile/', views.profile_view, name='profile'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # includes blog/urls.py
]

