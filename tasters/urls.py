from django.conf.urls import url

from tasters.views import ExportView
from . import views

urlpatterns = [
    url(
        r'^book/(?P<d>([0-9]{4}-[0-9]{2}-[0-9]{2}))?$',
        views.DateView.as_view(),
        name="Date, Time Select"
        ),
    url(
        r'^book/(?P<d>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<t>([0-9]{2}:[0-9]{2}))?$',
        views.DateTimeBookingView.as_view(),
        name="Date and Time, Activity Select / Form"
    ),
    url(
        r'^book/(?P<d>([0-9]{4}-[0-9]{2}-[0-9]{2}))/(?P<t>([0-9]{2}:[0-9]{2}))(/(?P<a>(sailing|windsurfing)))?$',
        views.DateTimeActivityBookingView.as_view(),
        name="Date and Time and Activity, Form"
    ),
    url(r'^sessions', views.BookView.as_view(), name="sessions"),
    url(r'^next-session/export', ExportView.as_view()),
    url(r'^$', views.index, name='home'),
]

