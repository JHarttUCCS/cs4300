from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from rest_framework import permissions

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .forms import *
from .models import *
from .views import *


# Create your views here.
# ==== Viewsets ====
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Movie.objects.all()
    #     else:
    #         return Movie.objects.none()


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# accounts
def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


def profile_redirect(request):
    return redirect('/movie_list/')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            # print(str(form.cleaned_data))

            return redirect("login")

    context = {}
    context['form'] = form

    return render(request, 'registration/register.html', context)


# page views
def index_redirect(request):
    return redirect('/movie_list/')


def movieList(request):
    context = {}

    movies = Movie.objects.all()
    context['movies'] = movies

    return render(request, 'BookingsApp/movie_list.html', context)


class BookingHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
        else:
            bookings = Booking.objects.none()

        context['bookings'] = bookings

        return render(request, 'BookingsApp/booking_history.html', context)


class SeatBookingView(LoginRequiredMixin, View):
    def get(self, request):
        form = BookingForm()
        context = {'form': form}
        return render(request, 'BookingsApp/seat_booking.html', context)

    def post(self, request):
        form = BookingForm(request.POST)

        print(form.errors)
        if form.is_valid():
            print("hi")

            booking_obj = form.save(commit=False)
            booking_obj.user = request.user

            booking_obj.save()

            return redirect('movie_list')
        
        context = {'form': form}
        return render(request, 'BookingsApp/seat_booking.html', context)


class SeatBookingViewID(LoginRequiredMixin, View):
    def get(self, request, movie_id):
        form = BookingForm(initial={'movie': movie_id})
        context = {'form': form}
        return render(request, 'BookingsApp/seat_booking.html', context)

    def post(self, request, movie_id):
        form = BookingForm(request.POST)

        print(form.errors)
        if form.is_valid():
            booking_obj = form.save(commit=False)

            # set user to current user in the booking object
            booking_obj.user = request.user
            booking_obj.save()
            
            # set the related seat to reserved in the booking object
            booking_obj.seat.status = Seat.RESERVED
            booking_obj.seat.save()

            return redirect('movie_list')
        
        context = {'form': form}
        return render(request, 'BookingsApp/seat_booking.html', context)
