from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^book', views.BookingView.as_view(), name="book"),
    url(r'^sessions', views.BookView.as_view(), name="sessions"),
    url(r'^reportkit', views.KitForm.as_view(), name="kit"),
    url(r'', views.index, name='home'),
]

