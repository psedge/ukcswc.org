from django.shortcuts import render
from django.http import HttpResponse
from .models import Date, Time

# Create your views here.
from django.views.generic import ListView


def index(req):
    return render(req, 'pages/index.html', {})

class BookView(ListView):
    template_name = 'pages/book.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        return Date.objects.order_by('date')

class Times(ListView):

    def get_queryset(self):
        return Time.objects.order_by('time')