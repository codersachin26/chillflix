from django.shortcuts import render
from .models import Movie_info,Movies,Movie_file,M_screenshots
from django.http import HttpResponse



def index(request):
    movie_info = Movie_info.objects.all()
    return render(request,'index.html',{'movie_info':movie_info})

def movie_info(request,id):
    movie = Movies.objects.get(movie_info=id)
    movies = Movie_info.objects.get(id=id)
    id_m = Movies.objects.filter(M_Categories=movie.M_Categories)
    screenshots = M_screenshots.objects.get(movie_info=id)
    m_related = []
    for i in id_m:
        if i.movie_info.id!=id:
            m_related.append(Movie_info.objects.get(id=i.movie_info.id))
        
    

    return render(request,'select_movie.html',{'movie':movie,'m':movies,'m_related':m_related,'i':screenshots})


def lates(request):
    m = Movie_info.objects.filter(M_released_date__gte='2020-3-8')
    return render(request,'index.html',{'movie_info':m})


def find_movie(request):
    movie_name = request.GET.get('search')
    movie = Movie_info.objects.get(M_name=movie_name)
    return render(request,'searchmovie.html',{'i':movie})


def about_us(request):
    return render(request,'AboutUs.html')


def contact(request):
    return render(request,'Contact.html')

    
def report(request):
    return render(request,'Report.html')


