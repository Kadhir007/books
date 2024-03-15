from django.contrib import admin
from bookshelf.models import Book, Genre, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
