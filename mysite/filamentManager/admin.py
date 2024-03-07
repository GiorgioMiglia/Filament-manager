from django.contrib import admin
from .models import Filament

class FilamentDisplay(admin.ModelAdmin):
    list_display = ('Material', 'Colour', 'Brand')

admin.site.register(Filament)