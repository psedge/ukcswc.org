from django.shortcuts import render, redirect
from .models import Date, Time
from .forms import SessionForm
from django.views.generic import ListView, FormView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(req):
    date = Date.objects.order_by('date').first()
    time = Time.objects.order_by('time').first()

    return render(req, 'pages/index.html', {
        'd': date,
        't': time
    })


class BookView(ListView):
    template_name = 'pages/sessions.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        return Date.objects.order_by('date')


class BookingView(FormView):
    template_name = 'pages/booking.html'
    form_class = SessionForm
    success_url = '/booked/'

    def get(self, context, **response_kwargs):
        date = Date.objects.get(date=response_kwargs['d'])
        time = Time.objects.get(time=response_kwargs['t'])
        if not date or not time:
            return HttpResponseRedirect('/tasters')

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'date': date.toHuman(),
            'time': time
        })

    def form_valid(self, form):
        form.valid()
        return super(BookingView, self).form_valid(form)

    def post(self, *context, **kwargs):
        return render(self.request, 'pages/index.html', {
            'message' : 'Thanks for booking! We\'ll send you a reminder the day before.',
        })

class Redirect(DetailView):
    def get(self, *context, **kwargs):
        return render(self.request, 'pages/index.html')

class BookingSuccess(Redirect):
    def get(self, *context, **kwargs):
        messages.success(self.request, 'Thanks for booking! We\'ll send you a reminder the day before.')
        return redirect('/')

