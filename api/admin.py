from django.contrib import admin
from .models import Movie, Rating #6 make register

# Register your models here.
admin.site.register(Movie) #6 new line
admin.site.register(Rating) #6 new line
