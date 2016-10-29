import markdown
import csv
import datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.http import HttpResponse
from announcements.models import Announcement
from content.models import Page, Event
from .forms import SessionForm, LoginForm
from .models import Date, UserSession, User


def index(req):
    today = datetime.datetime.today()

    pages = Page.objects.filter(published=True).all()
    date = Date.objects.filter(date__gte=today).order_by('date').first()
    event = Event.objects.filter(type='social', date__gte=today).order_by('date').first()
    announcements = Announcement.objects.order_by('-date').all()
    for announcement in announcements:
        announcement.html = markdown.markdown(announcement.text)

    return render(req, 'pages/index.html', {
        'd': date,
        'a': announcements,
        'p': pages,
        'e': event
    })


class BookView(ListView):
    template_name = 'pages/sessions.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        today = datetime.datetime.today()
        return Date.objects.filter(date__gte=today).order_by('date')


class DateView(DetailView):
    template_name = 'pages/dates.html'

    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])

        if not date:
            return HttpResponseRedirect('/sessions')

        return render(self.request, self.template_name, {
            'date': date,
        })


class DateBookingView(FormView):
    template_name = 'pages/booking.html'
    form_class = SessionForm

    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])
        self.form_class.declared_fields['activity'].initial = 'sailing'

        if not date:
            return HttpResponseRedirect('/sessions')

        # Check that time is valid for this day.

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'time': "11.00",
            'date': date.to_human(),
        })

    def form_valid(self, form):
        session = UserSession(
            user=User.objects.all().filter(Q(name=form.data['name']) | Q(kent_id=form.data['name'])).get(),
            date=Date.objects.filter(date=self.kwargs['d']).get(),
            time=self.kwargs['t'],
            activity=str(form.data['activity'])[0].upper()
        )

        try:
            session.validate_unique()
            session.save()
            messages.success(self.request, 'Thanks for booking! We\'ll send you a reminder the day before.')
            return redirect('/')
        except ValidationError:
            messages.error(self.request, 'Looks like you\'re already booked for that session.')
            return redirect('/')

    def form_invalid(self, form):
        messages.error(self.request, 'It appears you haven\'t signed up before. Please could you give us some details?')
        return redirect('/signup')


class DateTimeBookingView(DateBookingView):
    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])
        time = response_kwargs['t'] if response_kwargs['t'] in date.get_times() else "11.00"

        self.form_class.declared_fields['activity'].initial = 'sailing'

        if not date:
            return HttpResponseRedirect('/sessions')

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'date': date.to_human(),
            'time': time
        })


class DateTimeActivityBookingView(DateTimeBookingView):
    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])
        time = response_kwargs['t'] if response_kwargs['t'] in date.get_times() else "11.00"
        activity = response_kwargs['a']

        self.form_class.declared_fields['activity'].initial = activity

        if not date:
            return HttpResponseRedirect('/sessions')

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'date': date.to_human(),
            'time': time,
            'activity': activity
        })


class Redirect(DetailView):
    def get(self, *context, **kwargs):
        return redirect('/')


class BookingSuccess(Redirect):
    def get(self, *context, **kwargs):
        messages.success(self.request, 'Thanks for booking! We\'ll send you a reminder the day before.')
        return redirect('/')

class ExportView(DetailView):
    def get(self, request, *args, **kwargs):
        return self.render_to_response(request)

    def render_to_response(self, context, **response_kwargs):
        today = datetime.datetime.today()
        date = Date.objects.filter(date__gte=today).order_by('date').first()
        sessions = UserSession.objects.filter(date=date).iterator()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ukc-' + str(date.date) + '.csv"'

        writer = csv.writer(response)

        writer.writerow(['Shown up', 'Name', 'Kent ID', 'Time', 'Activity',])
        for session in sessions:
            writer.writerow(['', session.user.name, session.user.kent_id, session.time, session.activity])

        return response


class LoginView(DetailView):
    template_name = 'pages/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, {
            'form': self.form_class,
        })

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.all().filter(Q(kent_id=request.POST['name'])).get()
            return redirect('/user/' + user.kent_id)

        except User.DoesNotExist:
            messages.error(self.request, 'Can\'t find any bookings for that Kent ID / Username.')
            return redirect('/')


class UserView(DetailView):
    template_name = 'pages/user.html'

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.today()

        return render(self.request, self.template_name, {
            'id': kwargs['u'],
            'sessions': UserSession.objects.filter(user__kent_id=kwargs['u'], date__date__gte=today),
        })
