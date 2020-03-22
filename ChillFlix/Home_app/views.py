from django.shortcuts import render
from .models import Movie_info


def index(request):
    movie_info = Movie_info.objects.all()
    return render(request,'index.html',{'movie_info':movie_info})
