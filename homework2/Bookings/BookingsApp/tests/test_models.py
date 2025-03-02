import datetime

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
