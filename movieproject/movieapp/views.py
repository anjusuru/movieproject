from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages


# Create your views here.
def home(request):
    movie = Movie.objects.all()

    context = {
        'movie_list': movie
    }

    return render(request, 'home.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie_list': movie})

    # return HttpResponse('This is movie number %s' %movie_id)


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('txtName')
        desc = request.POST.get('txtDesc')
        img = request.FILES['fimage']
        year = request.POST.get('txtYear')
        movie = Movie(name=name, desc=desc, img=img, year=year)
        movie.save()
        messages.success(request, "movie added")
    return render(request, 'add.html')


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
