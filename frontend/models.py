from django.db import models
import time

# Create your models here.

class Date(models.Model):
    date = models.DateField("Date")

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

