from django.shortcuts import redirect
from .models import Feedback, KitReport
from tasters.models import User
from .forms import *
from django.views.generic import FormView
from django.contrib import messages


class KitFormView(FormView):
    template_name = 'pages/kitform.html'
    form_class = KitReportForm

    def form_valid(self, form):
        KitReport(
            area= form.data['area'],
            problem= form.data['problem']
        ).save()
        messages.success(self.request, 'Thanks for letting us know!')
        return redirect('/')


class FeedbackFormView(FormView):
    template_name = 'pages/feedback.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        Feedback(text=form.data['feedback']).save()
        messages.success(self.request, 'Thanks for your feedback, we\'ll bring this up with the committee.')
        return redirect('/')

class SignupFormView(FormView):
    template_name = 'pages/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        User(name=form.data['name'], kent_id=form.data['kent_id'], email=form.data['email'], mobile=form.data['mobile']).save()
        messages.success(self.request, 'Thanks for signing up, you can now book sessions with your name or Kent ID.')
        return redirect('/')


