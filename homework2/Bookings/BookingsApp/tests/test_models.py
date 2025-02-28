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
