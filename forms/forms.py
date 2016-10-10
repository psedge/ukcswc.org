from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions
from .validators import FeedbackValidator, KentIdValidator
from django.core.validators import EmailValidator

class KitReportForm(forms.Form):

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
        validators=[FeedbackValidator]
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('feedback',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Submit', 'Submit', css_class="btn-success"),
        )
    )


class SignupForm(forms.Form):

    name = forms.CharField(
        required= True,
        validators=[KentIdValidator],
        label="Full Name"
    )
    kent_id = forms.CharField(required=True, label="Kent Username (eg. jwc98)")
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator]
    )
    mobile = forms.IntegerField(required=False)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name',  css_class='form-control input-xlarge'),
        Field('kent_id',  css_class='form-control input-xlarge', name=""),
        Field('email',  type='email', css_class='form-control input-xlarge',),
        Field('mobile', css_class='form-control input-xlarge'),

        FormActions(
            Submit('Signup', 'Signup', css_class="btn-success"),
        )
    )
