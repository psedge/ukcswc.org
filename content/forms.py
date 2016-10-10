from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions
from django.contrib.admin.widgets import AdminDateWidget
from django_markdown.fields import *

from content.models import Event


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = MarkdownFormField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('title',  css_class='form-control input-xlarge'),
        Field('content',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Publish', 'Publish', css_class="btn-success"),
        )
    )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('type', 'date', 'title')

    type = forms.ChoiceField(
        choices=(('social', 'Social'), ('racing', 'Racing Event'), ('training', 'Training Session')),
    )
    date = forms.DateField()
    date.widget = AdminDateWidget(attrs=None, format='%Y-%m-%d')
    title = forms.CharField(max_length=100)
    facebook_link = forms.CharField(max_length=500, label="Facebook Link")

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('type',  css_class='form-control radio input-xlarge'),
        Field('title',  css_class='form-control input-xlarge'),
        Field('facebook_link',  css_class='form-control input-xlarge'),

        FormActions(
            Submit('Publish', 'Publish', css_class="btn-success"),
        )
    )