from django.db import models
import os
import datetime

# Create your models here.
class Movie_info(models.Model):
    M_name = models.CharField(max_length=50)
    M_type = models.CharField(max_length=15,default='movie')
    M_released_date = models.DateField()
    M_languages = models.CharField(max_length=30)
    M_img  = models.ImageField(upload_to='movie_poster/')
    M_quality = models.CharField(max_length=30)

    def __str__(self):
        return self.M_name




class Movies(models.Model):
    movie_info = models.ForeignKey('Movie_info',on_delete=models.CASCADE)
    M_story = models.CharField(max_length=500)
    M_time_length = models.DurationField()
    M_Categories = models.CharField(max_length=50)
    M_format = models.CharField(max_length=10)
    M_creator =models.CharField(max_length=20)
    M_pics = models.ImageField(upload_to='movie_pics')

    def __str__(self):
        return self.movie_info.M_name+' '+ self.M_creator



class Movie_file(models.Model):
    movie_info = models.ForeignKey('Movie_info',on_delete=models.CASCADE)
    _480p = models.FileField(upload_to='_480p')
    _720p = models.FileField(upload_to='_720p/' ,default='None')
    _1080p =models.FileField(upload_to='_1080p',default='None')

    def __str__(self):
        return self.movie_info.M_name+' files'




class M_screenshots(models.Model):
    movie_info = models.ForeignKey('Movie_info',on_delete=models.CASCADE)
    screenshot1 = models.ImageField(upload_to='img1', default='None')
    screenshot2 = models.ImageField(upload_to='img2',default='None')
    screenshot3 = models.ImageField(upload_to='img3',default='None')

    def __str__(self):
        return self.movie_info.M_name+' screenshots'



class UserComments(models.Model):
    movie_info = models.ForeignKey('Movie_info',on_delete=models.CASCADE)
    U_msg = models.CharField(max_length=100)
    U_Email_id = models.EmailField()
    U_name = models.CharField(max_length=25)
    cmt_date = models.DateTimeField(default= datetime.datetime.today())

    def __str__(self):
        return self.U_name


class Contact(models.Model):
    user_name = models.CharField(max_length=25)
    Email = models.EmailField()
    Subject = models.CharField(max_length=50)
    massage = models.CharField(max_length=300)

    def __str__(self):
        return self.user_name


class Reports(models.Model):
    user_name = models.CharField(max_length=25)
    Email = models.EmailField()
    movie_name = models.CharField(max_length=50)
    massage = models.CharField(max_length=300)

    def __str__(self):
        return self.movie_name
