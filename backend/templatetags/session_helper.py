from django import template
from tasters.models import Date
import datetime

register = template.Library()

# Turns out assingment tags are for objects, simple_tags are for strings.
# No idea why this worked locally.
@register.assignment_tag()
def next_session(*args):
    try:
        return Date.objects.all().filter(date__gte=datetime.date.today()).order_by('date').first()
    except:
        return False


@register.simple_tag
def get_activity(activity):
    return 'Sailing' if activity == 'S' else 'Windsurfing'
