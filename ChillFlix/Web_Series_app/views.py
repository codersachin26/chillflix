from django.shortcuts import render
from .models import Web_series,Series_info,Seasons,Episode,Episode_file

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
    season = Seasons.objects.using('web_series').get(season_no=s_no)
    
    seriesInfo = Series_info.objects.using('web_series').get(web_series = id)
    series = Web_series.objects.using('web_series').get(id=id)
    s_id =season.id
    episodes = Episode.objects.using('web_series').filter(season=s_id)
    
    return render(request,'Series_Season.html',{'series':series,'seriesinfo':seriesInfo,'season':season,'e':episodes})    

   