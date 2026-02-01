from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list view (optional)
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes from the router
    path('', include(router.urls)),
]