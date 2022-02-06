from django.shortcuts import render, redirect, reverse
from books import models as book_models
from movies import models as movie_models
from . import forms

def create_review(request, pk):
  kind = request.GET.get('kind', 'movie')

  if request.method == "POST":
    form = forms.CreateReviewForm(request.POST)
    movie = movie_models.Moive.objects.get_or_none(pk=pk)
    book = book_models.Book.objects.get_or_none(pk=pk)
    if kind == 'movie':
      if not movie:
        return redirect(reverse("core:home"))
      if form.is_valid():
        review = form.save()
        review.movie = movie
        review.user = request.created_by
        review.save()
        return redirect(reverse("movies:movie", kwargs={"pk":movie.pk}))

    if kind == 'book':
      if not book:
        return redirect(reverse("core:home"))