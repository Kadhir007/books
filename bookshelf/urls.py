from django.conf import settings
from django.conf.urls.static import static
from .views import BookListView, BookDetailView, BookCreateView, UpdateBookView, DeleteBookView,search_results
from django.urls import path

urlpatterns = [
    path('add/', BookCreateView.as_view(), name='add_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('update<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('search/', search_results, name='search_results'),
    path('', BookListView.as_view(), name='book_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
