from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reportkit', views.KitFormView.as_view(), name="reportkit"),
    url(r'^feedback', views.FeedbackFormView.as_view(), name="feedback"),
]