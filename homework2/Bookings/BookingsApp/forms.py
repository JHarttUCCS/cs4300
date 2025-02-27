from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class BookingForm(forms.ModelForm):
    # booking_date = forms.DateTimeField()
    # only show free seats for bookings
    seat = forms.ModelChoiceField(queryset=Seat.objects.filter(status=Seat.FREE))

    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'booking_date']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'groups']
