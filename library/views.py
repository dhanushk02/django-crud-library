from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# READ - list
def book_list(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'books': books})

# READ - detail
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

# CREATE
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect(book.get_absolute_url())
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)  
        if form.is_valid():
            book = form.save()
            return redirect(book.get_absolute_url())
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'book': book})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'book_confirm_delete.html', {'book': book})
