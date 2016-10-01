from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<p>([a-zA-Z\-]*))?$', views.PageView.as_view(), name="pages"),
]