from django.contrib import admin

class FeedbackAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ['text', 'date']
    list_display = ['text', 'date']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class KitFormAdmin(admin.ModelAdmin):
    actions = ['mark_as_solved']
    readonly_fields = ['problem', 'area', 'date']
    list_display = ('solved', 'problem','area', 'date')
    list_display_links = ['problem']

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

