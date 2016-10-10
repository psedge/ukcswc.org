from django.db import models
from django_markdown.models import *


class Page(models.Model):
    view_only = False

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    # Attributes
    published = models.BooleanField()
    title = models.CharField(max_length=100)
    content = MarkdownField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.content


class Event(models.Model):
    view_only = False

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    # Attributes
    type = models.CharField(max_length=20, null=False)
    date = models.DateField()
    title = models.CharField(max_length=100, null=False, default='Event Title')
    facebook_link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.title)
