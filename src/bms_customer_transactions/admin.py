from django.contrib import admin

# Register your models here.
from .models import bms_cu_booking_history, bms_cu_faviorate
admin.site.register(bms_cu_booking_history)
admin.site.register(bms_cu_faviorate)