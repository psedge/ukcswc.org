from django.core.validators import ValidationError
from .models import User
from django.db.models import Q

class BookingUserValid(object):

    def __init__(self, value, message=None):
        user = User.objects.all().filter(Q(name=value) | Q(kent_id=value))

        if not user:
            raise ValidationError('It looks like you haven\'t booked before, you need to sign up!')

        self.message = message


class LoginUserValid(object):

    def __init__(self, value, message=None):
        user = User.objects.all().filter(Q(kent_id=value))

        if not user:
            raise ValidationError('We can\'t find that ID / Username!')

        self.message = message