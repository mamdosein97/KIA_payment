from django.contrib import admin

# Register your models here.
from KIA_services.models import KIAService, KIAServiceField, KIATransaction

admin.site.register(KIAService)
admin.site.register(KIAServiceField)
admin.site.register(KIATransaction)
