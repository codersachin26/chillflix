from django.contrib import admin
from .models import Movie_info,Movies,M_screenshots,Movie_file


# Register your models here.
admin.site.register(Movie_info)
admin.site.register(Movies)

admin.site.register(Movie_file)

admin.site.register(M_screenshots)




