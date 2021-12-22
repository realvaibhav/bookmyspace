from django.shortcuts import render
from bms_users.models import bms_signup
from bms_customer_transactions.models import bms_cu_booking_history
from parking_lots.models import bms_pl_data, bms_pl_booking_history

# Create your views here.
def admin_homepage_view(request):
    users = bms_signup.objects.all()
    cu_users = bms_signup.objects.filter(user_type=1)
    pl_users = bms_signup.objects.filter(user_type=2)
    user_count = []
    user_count.append(cu_users.count())
    user_count.append(pl_users.count())
    cu_percentage = format(cu_users.count()/users.count() * 100, '.2f')
    pl_percentage = format(pl_users.count()/users.count() * 100, '.2f')
    bookings = bms_cu_booking_history.objects.all()
    nov_count = bms_cu_booking_history.objects.filter(booking_date__icontains='2021-11').count()
    oct_count = bms_cu_booking_history.objects.filter(booking_date__icontains='2021-10').count()
    dec_count = bms_cu_booking_history.objects.filter(booking_date__icontains='2021-12').count()
    booking_count = [0,0,0,0,0,0,0,0,0,oct_count, nov_count, dec_count]
    sum = 0
    for booking in bookings:
        sum = sum + booking.total_price_paid
    context = {
        "total_users_count" : users.count(),
        "customer_percentage" : cu_percentage,
        "pl_percentage" : pl_percentage,
        "user_count" : user_count,
        "total_bookings" : bookings.count(),
        "total_transaction_amount" : sum,
        'booking_count': booking_count

    }
    return render(request, "admin-homepage.html", context)