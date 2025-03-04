import datetime
import pytz

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import *
from ..serializers import *


class TestMoviesAPI(APITestCase):
    def setUp(self):
        self.author = User.objects.create(
            username='test_admin',
            email='test.admin@e.com',
            password='Test123',
            # is_superuser=True
        )
        self.client.force_authenticate(user=self.author)
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

    def test_list_movies(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = MovieSerializer([self.movie_obj], many=True).data
        self.assertEqual(response.data, serializer_data)

        # print(response)

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            'title': 'Never Existed 2',
            'description': 'What?!',
            'release_date': '2025-04-12',
            'duration': datetime.timedelta(
                hours=8,
                minutes=5,
                seconds=27
            )
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(title='Never Existed 2')
        self.assertEqual(movie.description, 'What?!')

    def test_create_movies_unauthenticated(self):
        self.client.logout()
        url = reverse('movie-list')
        data = {
            'title': 'Never Existed 2',
            'description': 'What?!',
            'release_date': '2025-04-12',
            'duration': datetime.timedelta(
                hours=8,
                minutes=5,
                seconds=27
            )
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_movie(self):
        url = reverse('movie-detail', args=[self.movie_obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = MovieSerializer(self.movie_obj).data
        self.assertEqual(response.data, serializer_data)

    def test_update_movie(self):
        url = reverse('movie-detail', args=[self.movie_obj.pk])
        data = {
            'title': 'Never Existed 2',
            'description': 'What?!',
            'release_date': '2025-04-12',
            'duration': datetime.timedelta(
                hours=8,
                minutes=5,
                seconds=27
            )
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie = Movie.objects.get(pk=self.movie_obj.pk)
        self.assertEqual(movie.title, 'Never Existed 2')

    def test_delete_movie(self):
        url = reverse('movie-detail', args=[self.movie_obj.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie_obj.pk).exists())


class TestSeatsAPI(APITestCase):
    def setUp(self):
        self.author = User.objects.create(
            username='test_admin',
            email='test.admin@e.com',
            password='Test123',
            # is_superuser=True
        )
        self.client.force_authenticate(user=self.author)
        self.seat_obj = Seat.objects.create(
            seat_num = 'G42',
            status = Seat.RESERVED,
            pk = 321
        )

    def test_list_seats(self):
        url = reverse('seat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = SeatSerializer([self.seat_obj], many=True).data
        self.assertEqual(response.data, serializer_data)

        # print(response)

    def test_create_seat(self):
        url = reverse('seat-list')
        data = {
            'seat_num': 'A23',
            'status': Seat.FREE,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        seat = Seat.objects.get(seat_num='A23')
        self.assertEqual(seat.status, Seat.FREE)

    def test_create_seat_unauthenticated(self):
        self.client.logout()
        url = reverse('seat-list')
        data = {
            'seat_num': 'A23',
            'status': Seat.FREE,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_seat(self):
        url = reverse('seat-detail', args=[self.seat_obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = SeatSerializer(self.seat_obj).data
        self.assertEqual(response.data, serializer_data)
    
    def test_update_seat(self):
        url = reverse('seat-detail', args=[self.seat_obj.pk])
        data = {
            'seat_num': 'A23',
            'status': Seat.FREE,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        seat = Seat.objects.get(pk=self.seat_obj.pk)
        self.assertEqual(seat.seat_num, 'A23')

    def test_delete_seat(self):
        url = reverse('seat-detail', args=[self.seat_obj.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Seat.objects.filter(pk=self.seat_obj.pk).exists())
    

class TestBookingsAPI(APITestCase):
    def setUp(self):
        self.author = User.objects.create(
            username='test_admin',
            email='test.admin@e.com',
            password='Test123',
            # is_superuser=True
        )
        self.client.force_authenticate(user=self.author)
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
            pk = 45 
        )
        self.booking_obj = Booking.objects.create(
            movie = Movie.objects.get(id=self.movie_obj.pk),
            seat = Seat.objects.get(id=self.seat_obj.pk),
            user = User.objects.get(id=self.user_obj.pk),
            booking_date = datetime.datetime(
                year=2024,
                month=3,
                day=2,
                hour=12,
                minute=30,
                tzinfo=pytz.UTC
            ),
            pk = 123
        )

    def test_list_bookings(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = BookingSerializer([self.booking_obj], many=True).data
        self.assertEqual(response.data, serializer_data)

        # print(response)

    def test_create_booking(self):
        url = reverse('booking-list')
        data = {
            'movie': self.movie_obj.pk,
            'seat': self.seat_obj.pk,
            'user': self.user_obj.pk,
            # 'booking_date': '2025-03-02T12:30:00Z'
            'booking_date': datetime.datetime(
                year=2025,
                month=3,
                day=2,
                hour=12,
                minute=30,
                tzinfo=pytz.UTC
            )
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # The only unique value I can pull by without creating a whole new object is booking_date
        booking = Booking.objects.get(booking_date=datetime.datetime(
            year=2025,
            month=3,
            day=2,
            hour=12,
            minute=30,
            tzinfo=pytz.UTC
        ))
        self.assertEqual(booking.seat.pk, 321)  

    def test_create_booking_unauthenticated(self):
        self.client.logout()
        url = reverse('booking-list')
        data = {
            'movie': self.movie_obj.pk,
            'seat': self.seat_obj.pk,
            'user': self.user_obj.pk,
            # 'booking_date': '2025-03-02T12:30:00Z'
            'booking_date': datetime.datetime(
                year=2025,
                month=3,
                day=2,
                hour=12,
                minute=30,
                tzinfo=pytz.UTC
            )
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_booking(self):
        url = reverse('booking-detail', args=[self.booking_obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = BookingSerializer(self.booking_obj).data
        self.assertEqual(response.data, serializer_data)
    
    def test_update_booking(self):
        url = reverse('booking-detail', args=[self.booking_obj.pk])
        data = {
            'movie': self.movie_obj.pk,
            'seat': self.seat_obj.pk,
            'user': self.user_obj.pk,
            # 'booking_date': '2025-03-02T12:30:00Z'
            'booking_date': datetime.datetime(
                year=2025,
                month=3,
                day=2,
                hour=12,
                minute=30,
                tzinfo=pytz.UTC
            )
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        booking = Booking.objects.get(pk=self.booking_obj.pk)
        self.assertEqual(booking.seat.pk, self.seat_obj.pk)

    def test_delete_booking(self):
        url = reverse('booking-detail', args=[self.booking_obj.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(pk=self.booking_obj.pk).exists())
