from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .validators import FeedbackValid


class KitForm(forms.Form):

    def valid(self):
        return True

    problem = forms.CharField(
        widget= forms.Textarea()
    )

    area = forms.ChoiceField(
        choices=(
            ('sailing', "The problem is to do with Sailing / Boat kit \n"),
            ('windsurfing', "The problem is to do with  Windsurfing kit \n"),
            ('clothing', "The problem is to do with items of clothing \n"),
        ),
        widget=forms.RadioSelect,
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('problem', css_class='form-control input-xlarge'),
        Field('area', css_class="radio"),
        FormActions(
            Submit('Report', 'Report', css_class="btn-success"),
        )
    )

class FeedbackForm(forms.Form):

    feedback = forms.CharField(
        widget= forms.Textarea(),
        required= True,
        validators=[FeedbackValid]
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('feedback',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Submit', 'Submit', css_class="btn-default"),
        )
    )
