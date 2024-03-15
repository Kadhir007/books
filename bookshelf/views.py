from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from bookshelf.models import Book
from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('book_list')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')

