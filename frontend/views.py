from django.shortcuts import render
from django.http import HttpResponse
from .models import Date, Time
from .forms import SessionForm, KitForm, FeedbackForm
from django.views.generic import ListView, FormView



def index(req):
    return render(req, 'pages/index.html', {})

class BookView(ListView):
    template_name = 'pages/book.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        return Date.objects.order_by('date')

class BookingView(FormView):
    template_name = 'pages/booking.html'
    form_class = SessionForm
    success_url = '/booked/'

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

