from django.contrib.admin import ModelAdmin

from forms import views
from tasters.forms import DateAdminForm


class UserSessionAdmin(ModelAdmin):
    list_display = ['id', 'user', 'activity', 'date', 'time']
    list_display_links = list_display

    def has_add_permission(self, request):
        return False


class DateAdmin(ModelAdmin):
    list_display = ['passed', 'date', 'spot_times', 'bookings']
    list_display_links = ['date']

    change_list_template = 'admin/date/change_list.html'
    form = DateAdminForm

    def has_add_permission(self, request):
        return True


class UserAdmin(ModelAdmin):
    list_display = ['id', 'name', 'kent_id', 'email', 'mobile']

    def has_add_permission(self, request):
        return True