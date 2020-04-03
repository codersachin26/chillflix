from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.web,name='web'),
    path('series_info/<int:id>',views.series_info,name='series_info'),
    path('series_info/season/<int:id>/<int:s_no>',views.season,name='season'),
    ]