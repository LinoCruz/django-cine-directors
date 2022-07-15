from django.contrib import admin

# Register your models here.
from .models import Director, Genre, Movie

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
