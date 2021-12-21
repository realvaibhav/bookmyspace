from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from bms_users.models import bms_signup
#from bms_customer_transactions.models import bms_cu_booking_history
from bms_customer_transactions.models import bms_cu_booking_history

# Create your models here.
# class parking_lot(models.Model):
#     name = models.CharField(max_length=50)
#     phonenumber = models.CharField(max_length=13, default='+91')
#     booking_price = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     opening_time = models.CharField(max_length=8)
#     closing_time = models.CharField(max_length=8)

class bms_pl_data(models.Model):
    pl_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("bms_users.bms_signup", on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    booking_price = models.PositiveIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    email = models.EmailField()
    total_slot_count = models.PositiveIntegerField()
    booked_slot_count = models.PositiveIntegerField()
    pl_image = models.ImageField(upload_to='pl-images/', null = True, default='pl-images/logo.jpg')
    pl_description = models.CharField(max_length=2500, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("parking-lot-details",kwargs={"pl_id" : self.pl_id})

class bms_pl_booking_history(models.Model):
    booking_id = models.AutoField(primary_key=True)
    pl_id = models.ForeignKey(bms_pl_data, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_code = models.ForeignKey(bms_cu_booking_history, on_delete=CASCADE)