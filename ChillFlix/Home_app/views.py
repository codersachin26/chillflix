from django.shortcuts import render
from .models import Movie_info
from django.http import HttpResponse


def index(request):
    movie_info = Movie_info.objects.all()
    return render(request,'index.html',{'movie_info':movie_info})

def movie_info(request,id):
    return HttpResponse(id)


def m(request):
    return render(request,'select_movie.html')

