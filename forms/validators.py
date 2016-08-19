from django.core.validators import ValidationError
from tasters.models import User

class FeedbackValidator(object):

    def __init__(self, value, message=None):
        if (len(value) < 10):
            raise ValidationError('Must be actual feedback.')
        if message:
            self.message = message


class KentIdValidator(object):

    def __init__(self, value, message=None):
        user = User.objects.all().filter(kent_id=value)

        if user:
            raise ValidationError('A user with that Kent ID already exists.')

        self.message = message