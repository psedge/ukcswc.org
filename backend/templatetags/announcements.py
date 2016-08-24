from django import template
from tasters.models import Date
from announcements.models import Announcement
from announcements.views import AnnouncementView

register = template.Library()

@register.simple_tag
def get_announcements():
    try:
        return Announcement.objects.all()
    except:
        return False

@register.simple_tag
def get_announcement_form():
    try:
        return AnnouncementView.as_view()
    except:
        return False
