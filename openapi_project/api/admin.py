from django.contrib import admin
from .models import Cinemas
# Register your models here.
# admin.site.register(Cinemas)
@admin.register(Cinemas)
class CinamesAdmin(admin.ModelAdmin):
    list_display_links = ('id','cinema_name', 'description',)
    list_display = ('id', 'cinema_name','address', 'website', 'description')