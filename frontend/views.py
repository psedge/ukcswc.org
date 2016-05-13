from django.shortcuts import render
from django.http import HttpResponse
from .models import Date

# Create your views here.
from django.views.generic import ListView


def index(req):
    return render(req, 'index.html', {})

class BookView(ListView):
    template_name = 'book.html'
    context_object_name = 'date_list'

    def get_queryset(self):
        return Date.objects.order_by('date')