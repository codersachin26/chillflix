from django.shortcuts import render
from .models import Web_series,Series_info,Seasons,Episode,Episode_file,Season_pics
from django.http import HttpResponse

# Create your views here.

def web(request):
    webseries = Web_series.objects.using('web_series').all()
    return render(request,'Web_Series.html',{'movie_info':webseries})





def series_info(request,id):
    seriesInfo = Series_info.objects.using('web_series').get(web_series = id)
    series = Web_series.objects.using('web_series').get(id=id)
    Seasons =[1,2,3,4,5,6]
    print("poster ",seriesInfo.categories)
    return render(request,'series_info.html',{'seriesinfo':seriesInfo,'series':series,'seasons':Seasons})


def season(request,id,s_no):
    season = Seasons.objects.using('web_series').get(season_no=s_no, web_series=id)
    quality = season.quality
    q = quality.split(' | ')
    seriesInfo = Series_info.objects.using('web_series').get(web_series = id)
    series = Web_series.objects.using('web_series').get(id=id)
    s_id =season.id
    episodes = Episode.objects.using('web_series').filter(season=s_id)
    s_pics = Season_pics.objects.using('web_series').filter(web_series=id)
    all_seasons = seriesInfo.seasons
    next_seasons = [s_pics,all_seasons]

    return render(request,'Series_Season.html',{'series':series,'q':q,'seriesinfo':seriesInfo,'season':season,'e':episodes,'next_seasons':s_pics})



def download_episode(request,Q,id):
    episode = Episode_file.objects.using('web_series').get(episode=id)
    
    
    if Q=="480p":
        p = episode._480p
        path = "media/"+str(p)
        fileopen = open(path,'rb')
        e_file = fileopen.read()
        
        f=episode._480p.name
     
    else:
        if Q=="720p":
            
            p = episode._720p
            path = "media/"+str(p)
            fileopen = open(path,'rb')
            e_file = fileopen.read()
            f = episode._720p.name
           
        else:
            if Q=="1080p":
                p = episode._1080p
                path = "media/"+str(p)
                fileopen = open(path,'rb')
                e_file = fileopen.read()
                f=episode._1080p.name
                
    
    response = HttpResponse(e_file,content_type='application/MP4')
    response['Content-Disposition'] = 'attachment; filename='+f
    return response   

   