from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='home page'),
    #path('movie_info/(?P<id>[0-9]+)/$',views.movie_info,name='movie_info')
    path('movie_info/<int:id>',views.movie_info,name='movie_info'),
    path('m',views.m,name='m')
]