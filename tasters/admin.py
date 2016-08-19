from django.contrib.admin import ModelAdmin

class UserSessionAdmin(ModelAdmin):
    list_display = ['id', 'user', 'activity', 'date', 'time']
    list_display_links = list_display

    def has_add_permission(self, request):
        return False


class DateAdmin(ModelAdmin):
    list_display = ['date', 'spots_left']
    actions = None

    def has_add_permission(self, request):
        return True


class UserAdmin(ModelAdmin):
    list_display = ['id', 'name', 'kent_id', 'email', 'mobile']

    def has_add_permission(self, request):
        return True