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
    cat = seriesInfo.categories
    series_cat = Series_info.objects.using('web_series').filter(categories = cat)
    related =[]
    
    for i in series_cat:
        ids = i.web_series
        if id!=ids.id:
            related.append(Web_series.objects.using('web_series').get(id = ids.id))

    all_seasons=[]
    for i in range(1,seriesInfo.seasons+1):
            all_seasons.append(i)

    return render(request,'series_info.html',{'m_related':related,'seriesinfo':seriesInfo,'series':series,'seasons':all_seasons})


def season(request,id,s_no):
    season = Seasons.objects.using('web_series').get(season_no=s_no, web_series=id)
    quality = season.quality
    q = quality.split(' | ')
    seriesInfo = Series_info.objects.using('web_series').get(web_series = id)
    series = Web_series.objects.using('web_series').get(id=id)
    s_id =season.id
    episodes = Episode.objects.using('web_series').filter(season=s_id)
    for i in episodes:
        print(i.id)
    s_poster = Season_pics.objects.using('web_series').get(season=s_id)
    s_pics = Season_pics.objects.using('web_series').filter(web_series=id)
    s_picss =[]
    for i in s_pics:
        if s_poster!=i.s_poster:
            s_picss.append(i)
    all_seasons =[]
    for i in range(1,seriesInfo.seasons+1):
        if i!=s_no:
            all_seasons.append(i)
    next_seasons = zip(s_picss,all_seasons)

    return render(request,'Series_Season.html',{'next_seasons':next_seasons,'series':series,'q':q,'seriesinfo':seriesInfo,'season':season,'e':episodes,'s_pics':s_poster})



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


def play_series(request,Q,id):
    episode = Episode_file.objects.using('web_series').get(episode=id)
    if Q=="480p":
        path = episode._480p
     
    else:
        if Q=="720p":
            path = episode._720p
           
        else:
            if Q=="1080p":
                path = episode._1080p

    return render(request,'play_series.html',{'path':path})
 