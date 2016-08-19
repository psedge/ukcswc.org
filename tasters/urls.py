from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book/(?P<d>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<t>([0-9]{2}:[0-9]{2}))(/(?P<a>(sailing|windsurfing)))?$', views.BookingView.as_view(), name="book"),
    url(r'^sessions', views.BookView.as_view(), name="sessions"),

    url(r'', views.index, name='home'),
]

