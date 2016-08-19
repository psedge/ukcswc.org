from django.contrib import admin

from tasters.models import *
from tasters.admin import *
from forms.models import *
from forms.admin import *

class UKCAdmin(admin.AdminSite):
    site_header = 'UKC Sailing and Windsurfing Administration'
    index_template = 'admin/backend/index.html'


admin_site = UKCAdmin(name='UKC')

admin_site.register(UserSession, UserSessionAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Date, DateAdmin)

admin_site.register(KitForm, KitFormAdmin)
admin_site.register(Feedback, FeedbackAdmin)