from django.contrib import admin
from content.forms import *
from content.models import Event, Page


class PageAdmin(admin.ModelAdmin):
    class Meta:
        model = Page
        fields = ('title', 'content')

    actions = None
    list_display = ['published', 'title']
    list_display_links = ('title',)
    form = PageForm

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ('type', 'date', 'title')

    actions = None
    list_display = ['type', 'date', 'title']
    list_display_links = ('title',)
    form = EventForm

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True