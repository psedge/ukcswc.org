from django.apps import AppConfig


class FormsConfig(AppConfig):
    name = 'Forms'
    label = 'Form Submissions'
    app_label = 'Form Submissions'

    super().label = 'Form Submissions'