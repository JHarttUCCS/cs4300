from django.urls import path, include
from rest_framework import routers

from . import views


# create router and register the viewsets
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')


urlpatterns = [
    # api urls
    path('api/', include(router.urls)),
    
    # page urls
    path('movie_list', views.movieList, name='movie_list'),
    path('booking_history', views.bookingHistory, name='booking_history'),
]
