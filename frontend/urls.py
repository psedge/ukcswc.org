from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^book/(?P<d>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<t>([0-9]{2}:[0-9]{2})$)', views.BookingView , name="book"),
    url(r'^sessions', views.BookView.as_view(), name="sessions"),
    url(r'^reportkit', views.KitForm.as_view(), name="reportkit"),
    url(r'^feedback', views.FeedbackForm.as_view(), name="feedback"),
    url(r'', views.index, name='home'),
]

