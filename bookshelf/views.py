from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from bookshelf.models import Book
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
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

def search_results(request):
    query = request.GET.get('query')
    results = Book.objects.none()
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query) | Q(genre__name__icontains=query)
        ).distinct()

    return render(request, 'list.html', {'book_list': results})