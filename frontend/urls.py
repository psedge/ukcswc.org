from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book', views.BookView.as_view(), name="book"),
    url(r'', views.index, name='home'),
]