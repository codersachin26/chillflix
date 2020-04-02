from django.shortcuts import render
from .models import Web_series

# Create your views here.

def web(request):
    webseries = Web_series.objects.using('web_series').all()
    return render(request,'Web_Series.html',{'movie_info':webseries})