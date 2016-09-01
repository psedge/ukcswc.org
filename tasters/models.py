import datetime

from django import forms
from django.db import models
from django.forms import MultipleChoiceField
from django.utils.html import format_html


class Time():
    choices = (
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
    )


class Date(models.Model):

    date = models.DateField("Date")

    times = models.CharField(
        max_length=255
    )

    def get_spots(self):
        """
        Get a list of Spots against the date.

        :return:
        """
        spots = []
        for time in self.times.split(', '):
            spots.append(Spot(time=time, date=self))
        return spots

    def get_total_sessions(self):
        return UserSession.objects.all().filter(date=self).count()


    def to_human(self):
        return self.date.strftime("%a %d/%m/%y")

    # Admin methods
    def passed(self):
        if (self.date <= datetime.date.today()):
            return format_html("<i class='fa fa-check'></i>")
        return format_html("<i class='fa fa-close'></i>")

    def bookings(self):
        return UserSession.objects.all().filter(
            date=self
        ).count()

    def spot_times(self):
        return self.times

    def get_times(self):
        return self.times.split(', ')

    # Magic methods
    def __str__(self):
        return str(self.date)


class Spot():
    SAILING_PLACES = 6
    WINDSURFING_PLACES = 6

    def __init__(self, date, time):
        self.date = date
        self.time = time

        # Counts
        self.places_sailing = self.SAILING_PLACES - UserSession.objects.all().filter(
            date=self.date, time=self.time, activity='S'
        ).count()
        self.places_windsurfing = self.WINDSURFING_PLACES - UserSession.objects.all().filter(
            date=self.date, time=self.time, activity='W'
        ).count()

        # Session objects
        self.sessions = UserSession.objects.all().filter(
            date=self.date, time=self.time
        )


class User(models.Model):
    name = models.CharField(max_length=50)
    kent_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, null=True)
    mobile = models.IntegerField(null=True)

    def __str__(self):
        return self.name + " - " + self.kent_id

    def id(self):
        return str(self.id)

class UserSession(models.Model):
    class Meta:
        verbose_name = 'Taster Session'
        verbose_name_plural = 'Taster Sessions'
        unique_together = ['user', 'date', 'time']

    def id(self):
        return str(self.user.id)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    time = models.CharField(max_length=5)
    activity = models.CharField(
        max_length=1,
        choices= ( ('S','Sailing'), ('W','Windsurfing')),
        default='S'
    )

    def __str__(self):
        return self.user.name + " - " + self.date.to_human() + " - " + str(self.time)

    def get_next_session(self):
        return self.objects.all().filter()


