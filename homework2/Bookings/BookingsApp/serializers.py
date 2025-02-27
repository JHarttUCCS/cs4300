from rest_framework import serializers
from .models import Movie, Seat, Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'duration']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_num', 'status']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking_date']
