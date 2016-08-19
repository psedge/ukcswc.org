from django import template
from tasters.models import Date
import datetime

register = template.Library()

@register.simple_tag
def next_session():
    try:
        date = Date.objects.all().filter(date__gt=datetime.date.today()).order_by('date').get()

        return date
    except:
        return False

@register.simple_tag
def get_activity(activity):
    return 'Sailing' if activity == 's' else 'Windsurfing'
