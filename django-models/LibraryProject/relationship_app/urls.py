from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ----------------------------
    # Book views
    # ----------------------------
    path('books/', views.list_books, name='list_books'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # ----------------------------
    # Library detail view
    # ----------------------------
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ----------------------------
    # User authentication
    # ----------------------------
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # ----------------------------
    # Role-based views
    # ----------------------------
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]
