from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer


# Create your views here.
# ==== Viewsets ====
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer = MovieSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
