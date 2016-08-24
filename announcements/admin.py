from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_markdown import models
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class AnnouncementAdmin(admin.ModelAdmin):

    actions = None
    readonly_fields = ('text'),
    verbose_name = 'Announcement'

    list_display = ('id', 'date', 'title', 'text','image')
    list_display_links = list_display

    formfield_overrides = {
        MarkdownFormField: {'widget': MarkdownWidget},
    }

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True
