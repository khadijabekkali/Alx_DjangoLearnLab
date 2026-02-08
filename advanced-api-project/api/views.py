from rest_framework import generics, filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer




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

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Filtering fields
    filterset_fields = ['title', 'publication_year', 'author']

    # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
