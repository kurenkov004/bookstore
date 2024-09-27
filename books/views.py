from django.shortcuts import render # type: ignore
from django.views.generic import ListView, DetailView # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from .models import Book

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
  model = Book
  template_name = 'books/main.html'

class BookDetailView(LoginRequiredMixin, DetailView):
  model = Book
  template_name = 'books/detail.html'