from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='home page'),
    #path('movie_info/(?P<id>[0-9]+)/$',views.movie_info,name='movie_info')
    path('movie_info/<int:id>',views.movie_info,name='movie_info'),
    path('lates/',views.lates,name='lates'),
    path('find_movie',views.find_movie,name='find_movie'),
     path('about_us',views.about_us,name='about_us'),
     path('contact',views.contact,name='about_us'),
     path('report',views.report,name='report'),

]