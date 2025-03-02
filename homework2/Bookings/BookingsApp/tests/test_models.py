import datetime
import pytz

from django.test import TestCase

from ..models import *


class TestMovies(TestCase):
    def setUp(self):
        self.movie_obj = Movie.objects.create(
            title = 'Never Existed',
            description = 'What?',
            release_date = '2024-04-12',
            duration = datetime.timedelta(
                hours=8,
                minutes=5,
                seconds=27
            ),
            pk = 42
        )
    
    def test_movie_pk(self):
        movie_pk = str(self.movie_obj.pk)
        movie_url = '/api/movies/' + movie_pk + '/'

        self.assertEqual(movie_url, self.movie_obj.get_absolute_url())

    def test_movie_instance(self):
        self.assertEqual(str(self.movie_obj), 'Never Existed')
        self.assertTrue(isinstance(self.movie_obj, Movie))


class TestSeats(TestCase):
    def setUp(self):
        self.seat_obj = Seat.objects.create(
            seat_num = 'G42',
            status = Seat.RESERVED,
            pk = 321
        )

    def test_seat_pk(self):
        seat_pk = str(self.seat_obj.pk)
        seat_url = '/api/seats/' + seat_pk + '/'

        self.assertEqual(seat_url, self.seat_obj.get_absolute_url())

    def test_seat_instance(self):
        self.assertEqual(str(self.seat_obj), 'G42')
        self.assertTrue(isinstance(self.seat_obj, Seat))


class TestBookings(TestCase):
    def setUp(self):
        self.movie_obj = Movie.objects.create(
            title = 'Never Existed',
            description = 'What?',
            release_date = '2024-04-12',
            duration = datetime.timedelta(
                hours=8,
                minutes=5,
                seconds=27
            ),
            pk = 42
        )

        self.seat_obj = Seat.objects.create(
            seat_num = 'G42',
            status = Seat.RESERVED,
            pk = 321
        )
        
        self.user_obj = User.objects.create(
            username='test_user',
            pk = 1
        )

        self.booking_obj = Booking.objects.create(
            movie = Movie.objects.get(id=42),
            seat = Seat.objects.get(id=321),
            user = User.objects.get(id=1),
            booking_date = datetime.datetime(
                year=2025,
                month=3,
                day=2,
                hour=12,
                minute=30,
                tzinfo=pytz.UTC
            ),
            pk = 123
        )

    def test_booking_pk(self):
        booking_pk = str(self.booking_obj.pk)
        booking_url = '/api/bookings/' + booking_pk + '/'

        self.assertEqual(booking_url, self.booking_obj.get_absolute_url())

    def test_booking_instance(self):
        self.assertEqual(str(self.booking_obj), 'Never Existed - G42')
        self.assertTrue(isinstance(self.booking_obj, Booking))
