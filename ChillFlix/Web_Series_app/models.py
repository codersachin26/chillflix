from django.db import models

# Create your models here.


class Web_series(models.Model):
    series_name = models.CharField(max_length=20)
    languages = models.CharField(max_length=25)
    released_date = models.DateField()
    series_poster = models.ImageField(upload_to='poster/')


    def __str__(self):
        return self.series_name




class Series_info(models.Model):
    web_series = models.ForeignKey('Web_series',on_delete=models.CASCADE)
    seasons = models.IntegerField()
    storyline = models.CharField(max_length=300)
    categories = models.CharField(max_length=30)
    creator = models.CharField(max_length=20)
    director = models.CharField(max_length=25,null=True)
    actors = models.CharField(max_length=100,null=True)
    format = models.CharField(max_length=10)
    poster = models.ImageField(upload_to='poster_pic/',null=True)
    

    def __str__(self):
        return self.web_series.series_name+' info'


class Seasons(models.Model):
    web_series = models.ForeignKey('Web_series',on_delete=models.CASCADE)
    season_no = models.IntegerField()
    quality = models.CharField(max_length=25,null=True)
    total_episodes = models.IntegerField()
    episodes_name = models.CharField(max_length=300)


    def __str__(self):
        return self.web_series.series_name+' season'+str(self.season_no)


class Episode(models.Model):
    season = models.ForeignKey('Seasons',on_delete=models.CASCADE)
    episode_name = models.CharField(max_length=30)
    e_no = models.IntegerField()
    e_duration = models.DurationField()

    def __str__(self):
        return self.season.web_series.series_name+' S'+str(self.season.season_no)+' E'+str(self.e_no)+self.episode_name


class Episode_file(models.Model):
    episode = models.ForeignKey('Episode',on_delete=models.CASCADE)
    _480p = models.FileField(upload_to='_480p/',default='none')
    _720p = models.FileField(upload_to='_720p/',default='none')
    _1080p = models.FileField(upload_to='_1080p/',default='none')

    def __str__(self):
        return self.episode.e_no+self.episode.episode_name



class Season_pics(models.Model):
    season = models.ForeignKey('Seasons',on_delete=models.CASCADE)
    s_poster = models.ImageField(upload_to='seasons_poster/')
    s_screenshot1 = models.ImageField(upload_to='screenshot1/')
    s_screenshot1 = models.ImageField(upload_to='screenshot2/')
    s_screenshot1 = models.ImageField(upload_to='screenshot3/')
