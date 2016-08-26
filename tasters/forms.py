from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import six

from tasters.fields import MultipleCheckboxField
from tasters.models import Date, Time
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

    date = forms.DateField()
    date.widget = AdminDateWidget(attrs=None, format='%Y-%m-%d')

    times = MultipleCheckboxField(
        choices=Time.choices,
        widget=CheckboxSelectMultipleWidget,
        validators=[],
    )

    base_fields = [date, times]

    def clean_times(self):
        return ', '.join(self.cleaned_data['times'])

    def is_valid(self):
        return True