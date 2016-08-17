from django.db import models
import time

class Date(models.Model):
    date = models.DateField("Date")

    def get_times(self):
        return Time.objects.order_by('time').iterator()

    def toHuman(self):
        return self.date.strftime("%a %d/%m/%y")

    def __str__(self):
        return str(self.date)


class Time(models.Model):
    time = models.TimeField("Time")

    def __str__(self):
        return self.time.strftime("%H:%M")

class User(models.Model):
    name = models.CharField(max_length=50)
    kent_id = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " - " + self.kent_id

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    activity = models.CharField(
        max_length=1,
        choices= ( ('S','Sailing'), ('W','Windsurfing')),
        default='S'
    )

    def __str__(self):
        return self.user.name + " - " + self.date.toHuman() + " - " + str(self.time)

