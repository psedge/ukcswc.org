from django.shortcuts import redirect
from django.views.generic import DetailView


class HomeRedirect(DetailView):
    def get(self, request, *args, **kwargs):
        return redirect('/')
