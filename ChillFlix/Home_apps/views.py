from django.shortcuts import render,redirect
from .models import Movie_info,Movies,Movie_file,M_screenshots,UserComments
from django.http import HttpResponse ,FileResponse




def index(request):
    movie_info = Movie_info.objects.all()
    return render(request,'index.html',{'movie_info':movie_info})

def movie_info(request,id):
    movie = Movies.objects.get(movie_info=id)
    movies = Movie_info.objects.get(id=id)
    id_m = Movies.objects.filter(M_Categories=movie.M_Categories)
    screenshots = M_screenshots.objects.get(movie_info=id)
    usercmts = UserComments.objects.filter(movie_info=id).order_by('-cmt_date')[:4]
    v = Movie_file.objects.get(id=1)
    p = v._480p
    m_qulaties = movies.M_quality
    Q = m_qulaties.split(' | ')
    m_related = []
    for i in id_m:
        if i.movie_info.id!=id:
            m_related.append(Movie_info.objects.get(id=i.movie_info.id))
        
    

    return render(request,'select_movie.html',{'movie':movie,'usercmts':usercmts,'Q':Q,'m':movies,'m_related':m_related,'i':screenshots,'kk':p})


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



def sendfile(request,ids,Q):
    m = Movie_file.objects.get(id=ids)
    if Q=="_480p":
        p = m._480p
        path = "media/"+str(p)
        fileopen = open(path,'rb')
        file = fileopen.read()
        f=m._480p.name
    else:
        if Q=="_720p":
            p = m._720p
            path = "media/"+str(p)
            fileopen = open(path,'rb')
            file = fileopen.read()
            f=m._720p.name 
        else:
            if Q=="_1080p":
                p = m._1080p
                path = "media/"+str(p)
                fileopen = open(path,'rb')
                file = fileopen.read()
                f=m._1080p.name
           
       

    response = HttpResponse(file, content_type='application/webm')
    response['Content-Disposition'] = 'attachment; filename='+f
    return response



def usercmt(request):
    msg = request.POST.get('usermsg')
    Email = request.POST.get('email')
    username = request.POST.get('username')
    id = request.POST.get('id')

    userdata = UserComments()
    userdata.U_msg = msg
    userdata.U_Email_id = Email
    userdata.movie_info = Movie_info.objects.get(id=id)
    userdata.U_name = username
    userdata.save()
    return redirect('movie_info',id)



