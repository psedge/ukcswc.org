from django.contrib import admin

from tasters.models import *
from forms.models import *

class UKCAdmin(admin.AdminSite):
    site_header = 'UKC Sailing and Windsurfing Administration'
    index_template = 'admin/index.html'

admin_site = UKCAdmin(name='UKC')

admin_site.register(UserSession)
admin_site.register(User)
admin_site.register(Date)

admin_site.register(KitForm)
admin_site.register(Feedback)