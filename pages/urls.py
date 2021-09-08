from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/movies', views.movies, name='movies'),
    path('/movie_detail', views.movieDetail, name='movie_detail'),
    path('/tv_shows', views.tvShows, name='tv_shows'),
    path('/premium', views.premium, name='premium'),
    path('/series', views.series, name='series'),
]
