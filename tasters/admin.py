from django.contrib.admin import ModelAdmin

class UserSessionAdmin(ModelAdmin):
    def has_add_permission(self, request):
        return False