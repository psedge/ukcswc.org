from django.forms import *
from django.forms.utils import flatatt
from django.forms.widgets import ChoiceInput, ChoiceFieldRenderer
from django.utils.encoding import force_text
from django.utils.html import format_html


class ChoiceSingleInput(ChoiceInput):
    """
    An object used by ChoiceFieldRenderer that represents a single
    <input type='$input_type'>.
    """
    input_type = None  # Subclasses must define this

    def __init__(self, name, value, attrs, choice, index):
        super().__init__(name, value, attrs, choice, index)

    def tag(self, attrs=None):
        attrs = attrs or self.attrs
        final_attrs = dict(attrs, type=self.input_type, name=self.name, value=self.choice_value)

        return format_html('<input{} />', flatatt(final_attrs))

class CheckboxChoiceInput(ChoiceSingleInput):
    input_type = 'checkbox'

    def __init__(self, *args, **kwargs):
        super(CheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.value = set(force_text(v) for v in self.value)
        if (self.choice_value in args[1]):
            self.attrs['checked'] = True

class CheckboxFieldRenderer(ChoiceFieldRenderer):

    choice_input_class = CheckboxChoiceInput


class CheckboxSelectMultipleWidget(CheckboxSelectMultiple):

    renderer = CheckboxFieldRenderer


