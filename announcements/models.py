from django.db import models
from django_markdown.models import *

class Announcement(models.Model):

    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=40, null=False, default="Announcement Title")
    text = MarkdownField()
    image = models.FileField(upload_to="static/img")

    def __str__(self):
        return self.title