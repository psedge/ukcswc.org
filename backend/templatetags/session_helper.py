from django import template
from tasters.models import Date
import datetime

register = template.Library()

@register.simple_tag
def next_session():
    try:
        return Date.objects.all().filter(date__gte=datetime.date.today()).order_by('date').first()
    except:
        return False

@register.simple_tag
def get_activity(activity):
    return 'Sailing' if activity == 's' else 'Windsurfing'
