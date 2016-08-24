from django.db import models
from django.views.generic import FormView
from django.contrib import admin
from .forms import AnnouncementForm


class AnnouncementView(FormView):
    form_class = AnnouncementForm
    template_name = 'pages/announcement.html'

    def form_valid(self, form):
        raise Exception(form)
        messages.success(self.request, 'Thanks for signing up, you can now book sessions with your name or Kent ID.')
        return redirect('/')

