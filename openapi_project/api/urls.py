from django.contrib import admin
from django.urls import path, include, re_path


from .views import CinemasViewSet
from rest_framework.routers import DefaultRouter


app_name = 'api'
router = DefaultRouter()
router.register('cinemas', CinemasViewSet, basename="cinemas")


urlpatterns = [
    path(r'', include(router.urls)),

]
