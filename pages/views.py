from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'pages/home.html')

def movies (request):
    return render (request, 'pages/movies.html')

def movieDetail (request):
    return render (request, 'pages/movie_detail.html')

def tvShows (request):
    return render (request, 'pages/tv_shows.html')

def premium (request):
    return render (request, 'pages/premium.html')

def series (request):
    return render (request, 'pages/series.html')