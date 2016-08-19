from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .validators import BookingUserValid

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

