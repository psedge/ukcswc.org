from django.contrib import admin

from content.admin import PageAdmin, EventAdmin, PhotoAdmin
from content.models import Page, Event, Photo
from tasters.models import *
from tasters.admin import *
from forms.models import *
from forms.admin import *
from announcements.models import *
from announcements.admin import *
from django_markdown.admin import MarkdownModelAdmin


class UKCAdmin(admin.AdminSite):
    site_header = 'UKC Sailing and Windsurfing Administration'
    index_template = 'admin/backend/index.html'



admin_site = UKCAdmin(name='UKC')

admin_site.register(UserSession, UserSessionAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Date, DateAdmin)

admin_site.register(KitReport, KitFormAdmin)
admin_site.register(Feedback, FeedbackAdmin)

admin_site.register(Announcement, AnnouncementAdmin)

admin_site.register(Page, PageAdmin)
admin_site.register(Photo, PhotoAdmin)
admin_site.register(Event, EventAdmin)

