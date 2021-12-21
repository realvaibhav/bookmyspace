from django.contrib import admin
from .models import bms_pl_data, bms_pl_booking_history
# Register your models here.
admin.site.register(bms_pl_data)
admin.site.register(bms_pl_booking_history)
