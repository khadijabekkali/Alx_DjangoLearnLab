from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from .models import Book

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Input validated
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
