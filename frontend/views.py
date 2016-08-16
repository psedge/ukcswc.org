from django.shortcuts import render
from .models import Date, Time
from .forms import SessionForm, KitForm, FeedbackForm
from django.views.generic import ListView, FormView, DetailView
from django.http import HttpResponseRedirect

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
            return HttpResponseRedirect('/sessions')

        return render(self.request, self.template_name, {
            'form': self.form_class,
            'date': date.toHuman(),
            'time': time
        })

    def form_valid(self, form):
        form.valid()
        return super(BookingView, self).form_valid(form)

class KitForm(FormView):
    template_name = 'pages/kitform.html'
    form_class = KitForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.valid()
        return super(KitForm, self).form_valid(form)

class FeedbackForm(FormView):
    template_name = 'pages/feedback.html'
    form_class = FeedbackForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.valid()
        return super(KitForm, self).form_valid(form)

class SuccessView(DetailView):

    def get(self, *context, **kwargs):

        return render(self.request, 'pages/success.html')