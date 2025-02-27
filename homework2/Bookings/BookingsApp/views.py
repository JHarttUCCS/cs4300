from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .views import *

# Create your views here.
# ==== Viewsets ====
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


# accounts
def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

def profile_redirect(request):
    return redirect('/movie_list')


# page views
def movieList(request):
    context = {}

    movies = Movie.objects.all()
    context['movies'] = movies

    return render(request, 'BookingsApp/movie_list.html', context)

def bookingHistory(request):
    context = {}

    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
    else:
        bookings = Booking.objects.none()

    context['bookings'] = bookings

    return render(request, 'BookingsApp/booking_history.html', context)
