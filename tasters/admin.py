from django.contrib.admin import ModelAdmin

from tasters.forms import DateAdminForm


class UserSessionAdmin(ModelAdmin):
    list_display = ['id', 'user', 'activity', 'date', 'time']
    list_display_links = list_display

    def has_add_permission(self, request):
        return False


class DateAdmin(ModelAdmin):
    list_display = ['date', 'spot_times', 'spots_left']
    # change_form_template = 'pages/tasters/date/change_form.html'
    form = DateAdminForm

    def has_add_permission(self, request):
        return True


class UserAdmin(ModelAdmin):
    list_display = ['id', 'name', 'kent_id', 'email', 'mobile']

    def has_add_permission(self, request):
        return True