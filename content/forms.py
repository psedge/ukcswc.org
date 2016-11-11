from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions
from django.contrib.admin.widgets import AdminDateWidget
from django_markdown.fields import *

from content import fields
from content.models import Event
from content.widgets import MultipleImageInput


class PageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('title', css_class='form-control input-xlarge'),
            Field('image', css_class='form-control input-xlarge'),
            HTML("<p>Please format this in Markdown. For help, please click <a href=\"help\">here</a></p>"),
            Field('content', css_class='form-control input-xlarge'),

            FormActions(
                Submit('Publish', 'Publish', css_class="btn-success"),
            )
        )
        super(PageForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length=100)
    image = fields.MultipleImageField()
    image.widget = MultipleImageInput()
    image.widget.clear_checkbox_label = 'Remove\n'
    help = Button(name="help-button", value="Content must be formatted in Markdown. For help, please click here")
    content = MarkdownFormField()

    def save(self, commit=True):
        m = super(PageForm, self).save(commit=False)

        if 'image-clear' in self.data and self.data['image-clear'] == 'on':
            m.image = None
            commit = True

        if commit:
            m.save()
        return m


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