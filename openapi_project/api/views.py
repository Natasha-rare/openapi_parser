from django.shortcuts import render
from rest_framework import viewsets, status, generics, views
from .models import Cinemas
from rest_framework import filters
from .serializers import CinemasSerilizer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
class CinemasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cinemas.objects.all()
    serializer_class = CinemasSerilizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cinema_name', 'address', 'description', 'legal_entity', 'website', 'category', 'inn']
    # filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # filterset_fields = ['cinema_name', 'address', 'description', 'legal_entity', 'website', 'category', 'inn']

