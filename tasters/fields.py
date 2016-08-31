from django.core.exceptions import ValidationError
from django.forms import MultipleChoiceField


class MultipleCheckboxField(MultipleChoiceField):

    def init(self, *args, **kwargs):
        super(MultipleCheckboxField, self).__init__(self, *args, **kwargs)
        super().widget_attrs({'checked': 'checked'})


    def validate(self, value):
        return True

    # def to_python(self, value):
    #     return value

    def full_clean(self):
        return True