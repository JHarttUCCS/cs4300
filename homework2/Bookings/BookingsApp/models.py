from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])


class Seat(models.Model):
    seat_num = models.CharField(max_length=3) # e.g. K16
    
    # status
    FREE = 0
    RESERVED = 1
    STATUS_CHOICES = [
        (FREE, "Free"),
        (RESERVED, "Reserved"),
    ]
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=FREE,
    )

    def __str__(self):
        return self.seat_num

    def get_absolute_url(self):
        return reverse('seat-detail', args=[str(self.id)])
        

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.movie} - {self.seat}"

