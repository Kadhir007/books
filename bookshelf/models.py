from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, related_name='books' ,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    genre = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title[:10]
