from django.contrib import admin
from .models import Book  # <-- this is required

# Customize the Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show in list view
    list_filter = ('author', 'publication_year')            # sidebar filters
    search_fields = ('title', 'author')                     # search box

# Register the Book model with the customized admin
admin.site.register(Book, BookAdmin)
