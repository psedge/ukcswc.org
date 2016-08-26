from django.core.exceptions import ValidationError
from django.forms import MultipleChoiceField


class MultipleCheckboxField(MultipleChoiceField):

    def validate(self, value):
        return True

    # def to_python(self, value):
    #     return value

    def full_clean(self):
        return True