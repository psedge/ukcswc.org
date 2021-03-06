import datetime

import requests
from django import forms
from django.db import models
from django.forms import MultipleChoiceField
from django.utils.html import format_html


class Time:
    choices = (
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
    )


class Date(models.Model):

    date = models.DateField("Date")
    times = models.CharField(max_length=255)
    sailing_spots = models.IntegerField(default=6)
    windsurfing_spots = models.IntegerField(default=6)

    def get_spots(self):
        """
        Get a list of Spots against the date.

        :return:
        """
        spots = []
        for time in self.times.split(', '):
            spots.append(Spot(time=time, date=self, sailing_spots=self.sailing_spots, windsurfing_spots=self.windsurfing_spots))
        return spots

    def get_total_sessions(self):
        return UserSession.objects.all().filter(date=self).count()

    def to_human(self):
        return self.date.strftime("%a %d/%m/%y")

    # Admin methods
    def passed(self):
        if self.date <= datetime.date.today():
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

    def __str__(self):
        return str(self.date)


class Spot:

    def __init__(self, date, time, sailing_spots, windsurfing_spots):
        self.date = date
        self.time = time

        # Counts
        self.places_sailing = sailing_spots - UserSession.objects.all().filter(
            date=self.date, time=self.time, activity='S'
        ).count()
        self.places_windsurfing = windsurfing_spots - UserSession.objects.all().filter(
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
        choices=(('S', 'Sailing'), ('W', 'Windsurfing')),
        default='S'
    )

    def __str__(self):
        return self.user.name + " - " + self.date.to_human() + " - " + str(self.time)

    def get_next_session(self):
        return self.objects.all().filter()

    def send_confirmation(self):
        try:
            requests.post(
                "https://api.mailgun.net/v3/ukcswc.org/messages",
                auth=("api", "key-e24d6abeb59ebd1397dc77493f25efd2"),
                data={"from": "UKCSWC <noreply@ukcswc.org>",
                      "to": [self.user.email],
                      "subject": self.activity + " session on " + self.date.to_human() + "!",
                      "text": "Hi " + self.user.name + ",\n\n" +

                      "Thanks for booking a session on " + self.date.to_human() + " at " + self.time +
                      "Please arrive at least 15 minutes before the session begins.\n\n" +

                      "At Whitstable Sailing Club, we have most of the kit you will need for your session, but " +
                      "we do recommend you bring the following items: A towel, a change of clothes, and some change " +
                      "for warm drinks or food.\n\n" +

                      "You can find details about Whitstable Yacht Club on their website at http://wyc.org.uk, or " +
                      "if you need further details about the session, please get in touch via our Facebook or " +
                      "Twitter pages.\n\n" +

                      "Thanks, UKCSWC.\n"
                      })
            return True
        except Exception as e:
            return False


