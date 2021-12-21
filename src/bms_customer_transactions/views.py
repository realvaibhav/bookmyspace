from django.shortcuts import render
from .models import bms_cu_booking_history, bms_cu_faviorate
from django.core.cache import cache
from parking_lots.models import bms_pl_data
from bms_users.models import bms_signup

# Create your views here.
def booking_history_view(get):
    query_set = bms_cu_booking_history.objects.filter(user_id = cache.get('loggedin_user_id')).order_by('-booking_date')
    print(type(query_set))
    if query_set.count() == 0:
        context = {
            "no_data_message":"You have not made any bookings"
        }
        return render(get, "cu-booking-history.html", context)
    else:
        # Bookings = query_set
        # print(type(Bookings))
        # for booking in query_set:
        #     pl_id = booking.pl_id
            # pl_user_id = booking.user_id
            # pl_data = bms_pl_data.objects.get(pl_id = pl_id)
            # booking["manager_name"] = pl_data.manager_name
            # booking["city"] = pl_data.city
            # booking["address"] = pl_data.address
            # booking["parking_lot_name"] = bms_signup.objects.get(user_id = pl_user_id).name
        context = {
            "no_data_message":"",
            "bookings" : query_set
        }
        return render(get, "cu-booking-history.html", context)

def fav_pl_view(get):
    query_set = bms_cu_faviorate.objects.filter(user_id = cache.get('loggedin_user_id'))
    if query_set.count() == 0:
        context = {
            "no_data_message" : "You have no faviorates"
        }
    else:
        context = {
            "no_data_message" : "",
            "fav_pl" : query_set
        }
    return render(get, "cu-fav-pl.html", context)