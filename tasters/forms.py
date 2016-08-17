from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms


class SessionForm(forms.Form):

    def valid(self):
        raise Exception(self)

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

#
# def post(self, request, *args, **kwargs):
#     if (self.form_valid()):
#         Feedback(text=request.POST.get('feedback')).save()
#
#     return render(self.request, 'pages/index.html', {
#         'message': 'Thanks for your feedback. We\'ll raise this with the Committee.'
#     })



