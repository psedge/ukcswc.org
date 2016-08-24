from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions
from django_markdown.models import MarkdownWidget, MarkdownField
from django_markdown.fields import *


class AnnouncementForm(forms.Form):

    date = forms.DateField(show_hidden_initial=True)
    text = MarkdownFormField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('text',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Publish', 'Publish', css_class="btn-success"),
        )
    )