from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
import markdown

from .models import Date, Time, UserSession, User
from announcements.models import Announcement
from .forms import SessionForm

def index(req):
    announcements = Announcement.objects.order_by('date').all()
    for announcement in announcements:
        announcement.html = markdown.markdown(announcement.text)

    return render(req, 'pages/index.html', {
        'd': Date.objects.order_by('date').first(),
        't': Time.objects.order_by('time').first(),
        'a': announcements
    })


class BookView(ListView):
    template_name = 'pages/sessions.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        return Date.objects.order_by('date')


class BookingView(FormView):
    template_name = 'pages/booking.html'
    form_class = SessionForm

    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])
        time = Time.objects.get(time=response_kwargs['t'])
        self.form_class.declared_fields['activity'].initial = response_kwargs['a']

        if not date or not time:
            return HttpResponseRedirect('/sessions')

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'date': date.to_human(),
            'time': time,
        })

    def form_valid(self, form):
        user = UserSession(
            user=User.objects.all().filter(Q(name=form.data['name']) | Q(kent_id=form.data['name'])).get(),
            date=Date.objects.filter(date=self.kwargs['d']).get(),
            time=Time.objects.filter(time=self.kwargs['t']).get(),
            activity=str(form.data['activity'])[0].upper()
        )

        try:
            user.validate_unique()
            user.save()
            messages.success(self.request, 'Thanks for your booking, we\'ll let you know closer to the time.')
            return redirect('/')
        except ValidationError:
            messages.error(self.request, 'Looks like you\'re already booked for that session.')
            return redirect('/')


    def form_invalid(self, form):
        messages.error(self.request, 'It appears you haven\'t signed up before. Please could you give us some details?')
        return redirect('/signup')

class Redirect(DetailView):
    def get(self, *context, **kwargs):
        return render(self.request, 'pages/index.html')

class BookingSuccess(Redirect):
    def get(self, *context, **kwargs):
        messages.success(self.request, 'Thanks for booking! We\'ll send you a reminder the day before.')
        return redirect('/')

