from rest_framework import generics, filters   # <-- must import filters
from django_filters import rest_framework      # <-- must import django_filters.rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering support.

    Filtering:
    - title
    - publication_year
    - author

    Searching:
    - title
    - author name

    Ordering:
    - title
    - publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Use filters.OrderingFilter and filters.SearchFilter
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']