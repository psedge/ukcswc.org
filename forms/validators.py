from django.core.validators import ValidationError

class FeedbackValid(object):

    def __init__(self, value, message=None):
        if (len(value) < 10):
            raise ValidationError('Must be actual feedback.')
        if message:
            self.message = message