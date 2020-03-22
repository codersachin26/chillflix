from django.db import models

# Create your models here.
class Movie_info(models.Model):
    M_name = models.CharField(max_length=50)
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

