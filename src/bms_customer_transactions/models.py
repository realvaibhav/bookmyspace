from django.db import models
from django.db.models.deletion import CASCADE
from bms_users.models import bms_signup
#from parking_lots.models import bms_pl_data
import parking_lots.models

# Create your models here.
class bms_cu_booking_history(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(bms_signup, on_delete=CASCADE)  #user_id of customer
    pl_id = models.ForeignKey("parking_lots.bms_pl_data", on_delete=CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateField(auto_now=False, auto_now_add=False)
    booked_time = models.TimeField()
    no_of_hours = models.IntegerField()
    total_price_paid = models.IntegerField()
    mode_of_payment = models.CharField(max_length=20, default = 'Offline')
    feedback = models.CharField(null = True, max_length=2000)

class bms_cu_faviorate(models.Model):
    fav_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(bms_signup, on_delete=CASCADE)
    pl_id = models.ForeignKey("parking_lots.bms_pl_data", on_delete=CASCADE)