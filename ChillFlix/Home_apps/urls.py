from django.conf.urls import url
from django.urls import path,include
from . import views
urlpatterns =[
  
    path('',views.index,name='home page'),
    path('categories',views.categories,name='categories'),
    path('movie_info/<int:id>',views.movie_info,name='movie_info'),
    path('lates/',views.lates,name='lates'),
    path('web', include('Web_Series_app.urls')),
    path('movie_info/sendfile/<int:ids>/<str:Q>/',views.sendfile,name='sendfile'),
    path('movie_info/usercmt',views.usercmt,name='usercmt'),
    path('about_us',views.about_us,name='about_us'),
    path('contact/',views.contact,name='contact'),
    path('report',views.report,name='report'),
    path('nextpage/<int:no>',views.nextpage,name='nextpage'),
    path('movie_info/movieplay/<int:id>',views.movieplay,name='movieplay'),





]
