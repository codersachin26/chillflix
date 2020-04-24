from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.web,name='web'),
    path('series_info/<int:id>',views.series_info,name='series_info'),
    path('series_info/season/<int:id>/<int:s_no>',views.season,name='season'),
    path('download/<str:Q>/<int:id>',views.download_episode,name='download_episode'),
    path('play_series/<str:Q>/<int:id>',views.play_series,name='play_series'),
    path('nextpage/<int:no>',views.nextpage,name='nextpage'),
    path('series_info/usercmt',views.usercmt,name='usercmt'),

    ]