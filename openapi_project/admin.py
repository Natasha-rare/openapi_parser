from django.contrib import admin
from .models import Cinemas
import os
# Register your models here.
# print('i am here', os.listdir('/'), os.listdir())
# admin.site.register(Cinemas)
@admin.register(Cinemas)
class CinamesAdmin(admin.ModelAdmin):
    list_display_links = ('id','cinema_name', 'description',)
    list_display = ('id', 'cinema_name','address', 'website', 'description')