from django.contrib import admin

class FeedbackAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ['text']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class KitFormAdmin(admin.ModelAdmin):
    actions = ['view']
    readonly_fields = ['problem', 'area']

    def view(self):
        return

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

