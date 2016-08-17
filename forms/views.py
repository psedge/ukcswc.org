from django.shortcuts import redirect
from .models import Feedback
from .forms import KitForm, FeedbackForm
from django.views.generic import FormView
from django.contrib import messages


class KitFormView(FormView):
    template_name = 'pages/kitform.html'
    form_class = KitForm

    def form_valid(self, form):
        KitForm(
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
