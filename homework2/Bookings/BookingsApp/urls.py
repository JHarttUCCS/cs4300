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

    # auth urls
    path('accounts/logout/', views.custom_logout, name='logoutView'),
    path('accounts/profile/', views.profile_redirect),
    path('accounts/register/', views.register, name='registerView'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # page urls
    path('', views.index_redirect),
    path('movie_list/', views.movieList, name='movie_list'),
    path('booking_history/', views.BookingHistoryView.as_view(), name='booking_history'),
    path('seat_booking/', views.SeatBookingView.as_view(), name='seat_booking'),
    path('seat_booking/<int:movie_id>/', views.SeatBookingViewID.as_view(), name='seat_booking_id'),
]
