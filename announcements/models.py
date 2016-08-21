from django.db import models
from django.forms.fields import DateField


class Announcement(models.Model):
    hero_image = 'static/ukc.jpg'
    date = DateField()
    text = models.TextField(max_length=None)