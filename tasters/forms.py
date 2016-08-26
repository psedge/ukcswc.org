from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import six

from tasters.fields import MultipleCheckboxField
from tasters.models import Date
from .validators import BookingUserValid
from .widgets import CheckboxSelectMultipleWidget

class SessionForm(forms.Form):

    name = forms.CharField(
        label='Name / Kent ID',
        validators= [BookingUserValid]
    )
    activity = forms.MultipleChoiceField(
        choices=(
            ('sailing', "Sailing"),
            ('windsurfing', 'Windsurfing'),
        ),
        widget=forms.CheckboxSelectMultiple,
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name', css_class='form-control input-xlarge'),
        Field('activity', css_class='checkbox input-xlarge'),
        FormActions(
            Submit('save_changes', 'Confirm booking', css_class="btn-success"),
        )
    )


class DateAdminForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ('date', 'times')

    date = forms.DateField(
        label='Date',
        widget=AdminDateWidget
    )
    times = MultipleCheckboxField(
        choices=(
            ('10.30', '10:30'),
            ('11.00', '11:00'),
            ('11.30', '11:30'),
            ('12.00', '12:00'),
            ('12.30', '12:30'),
            ('13.00', '13:00'),
            ('13.30', '13:30'),
            ('14.00', '14:00'),
            ('14.30', '14:30'),
        ),
        widget=CheckboxSelectMultipleWidget,
        validators=[],
    )

    base_fields = [date, times]

    def save(self, commit=True):
        times = dict(six.iterlists(self.data))
        date = Date(date=self.data['date'], times=times)
        date.save()