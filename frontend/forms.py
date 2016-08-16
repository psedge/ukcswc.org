from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SessionForm(forms.Form):

    def valid(self):
        return

    name = forms.CharField()
    activity = forms.MultipleChoiceField(
        choices=(
            ('sailing', "Sailing"),
            ('windsurfing', 'Windsurfing'),
        ),
        initial='sailing',
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

class KitForm(forms.Form):

    def valid(self):
        return True

    problem = forms.CharField(
        widget= forms.Textarea()
    )

    activity = forms.MultipleChoiceField(
        choices=(

        ),
        initial='sailing',
        widget=forms.CheckboxSelectMultiple,
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

    def is_valid(self):
        return True

    feedback = forms.CharField(
        widget= forms.Textarea()
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('feedback',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Submit', 'Submit', css_class="btn-default"),
        )
    )





