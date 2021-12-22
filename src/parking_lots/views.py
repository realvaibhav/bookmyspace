from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect

from bms_users.models import bms_signup
from .forms import pl_register_form
from .models import bms_pl_data, bms_pl_booking_history
from django.core.cache import cache
import requests
from bms_customer_transactions.models import bms_cu_booking_history, bms_cu_faviorate
from bms_customer_transactions.views import booking_history_view, fav_pl_view
from datetime import datetime
from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage
import os
from twilio.rest import Client

# Create your views here.

# def available_parking_lot_view(get):
#     if get.method == "GET":
#         available_PL = parking_lot.objects.all()
#         context = {
#             'parking_lots' : available_PL
#         }
#         return render(get, "parking-lots.html", context)


#pure django form
# def register_pl_view(requests):
#     pl_data = pl_register_form()
#     if requests.method == "POST":
#         pl_data = pl_register_form(requests.POST or None)
#         if pl_data.is_valid():
#             if cache.get('loggedin_user_id') == None:
#                 print('laude lag gaye')
#             else:
#                 print(cache.get('user_id'))
#                 #print(requests.session['user_id'])
#                 pl_data.cleaned_data['user_id'] = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
#                 pl_data.cleaned_data['booked_slot_count'] = 0
#                 bms_pl_data.objects.create(**pl_data.cleaned_data)
#                 return redirect(pl_homepage_view)
#     context = {
#         'register_form': pl_register_form,
#         'error_message': ''
#     }
#     return render(requests, "Register-parking-lot.html", context)

#raw html form
def register_pl_view(request):
    manager_name = request.POST.get('manager_name')
    address = request.POST.get('address')
    city = request.POST.get('city')
    booking_price = request.POST.get('booking_price')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')
    email = request.POST.get('email')
    total_slots_count = request.POST.get('total_slots_count')
    
    if request.method == "POST":
        temp = datetime.strptime(opening_time, "%I:%M %p")
        opening_time = datetime.strftime(temp, "%H:%M")
        temp = datetime.strptime(closing_time, "%I:%M %p")
        closing_time = datetime.strftime(temp, "%H:%M")
        pl_data = {
            "manager_name": manager_name,
            "address": address,
            "city": city,
            "booking_price": booking_price,
            "opening_time": opening_time,
            "closing_time": closing_time,
            "email": email,
            "total_slot_count": total_slots_count,
            "booked_slot_count": 0
        }
        
        if cache.get('loggedin_user_id') == None:
            print('laude lag gaye')
        else:
            print(cache.get('loggedin_user_id'))
            #print(request.session['user_id'])
            pl_data['user_id'] = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
            bms_pl_data.objects.create(**pl_data)
            print(pl_data)
            return redirect(pl_homepage_view)
    context = {
        'error_message': ''
    }
    return render(request, "register-pl.html", context)

def parking_lot_detail_view(request, pl_id):
    pl_data = bms_pl_data.objects.get(pl_id = pl_id)
    context = {
        "parking_lot" : pl_data,
        "slots_left": (pl_data.total_slot_count-pl_data.booked_slot_count)
    }
    if request.method == "POST":
        if 'add_to_fav' in request.POST:
            add_to_fav = request.POST.get('add_to_fav')
            fav_data = {
                "user_id" : bms_signup.objects.get(user_id = cache.get('loggedin_user_id')),
                "pl_id" : pl_data

            }
            bms_cu_faviorate.objects.create(**fav_data)
            return redirect(fav_pl_view)
        elif 'book_pl' in request.POST:
            no_of_hours = int(request.POST.get('hours'))
            booked_date = request.POST.get('booked_date')
            booked_time = request.POST.get('booked_time')
            user_data = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
            booking_data = {
                'user_id' : user_data,
                "pl_id" : pl_data,
                "total_price_paid" : (pl_data.booking_price * no_of_hours),
                "no_of_hours" : no_of_hours,
                "booked_date" : booked_date,
                "booked_time" : booked_time
            }
            print(booking_data)
            booking_code = bms_cu_booking_history.objects.create(**booking_data)
            booking_data_pl = {
                "pl_id": pl_data,
                "booking_code": booking_code,
            }
            bms_pl_booking_history.objects.create(**booking_data_pl)
            billing_amount = str(pl_data.booking_price * no_of_hours)
            email_message = user_data.name + " have booked a slot in your parking Lot. \nBooked Time: "+ booked_time +" "+ booked_date + "\nDuration: " + str(no_of_hours) + " hours" + "\nTotal Billing amount: ₹" + billing_amount
            send_email("New Slot Booked", email_message, "pxyz220@gmail.com")

            sms_message = "Hello, " + user_data.name + " You have successfully booked a slot at " + pl_data.user_id.name + "\nBooked Time: "+ booked_time +" "+ booked_date + "\nDuration: " + str(no_of_hours) + " hours" + "\nTotal Billing amount: ₹" + billing_amount
            send_sms(user_data.phonenumber, sms_message)

            sms_message_pl = "Hello " + pl_data.user_id.name + "," + user_data.name+ " have booked a slot in your parking Lot. Booked Time: "+ booked_time +" "+ booked_date + " Duration: " + str(no_of_hours) + " hours" + " Total Billing amount: ₹" + billing_amount
            #send_sms(pl_data.user_id.phonenumber, sms_message_pl)

            return redirect(booking_history_view)
        
    return render(request, "parking-lot-detail.html", context)

def pl_booking_history_view(get):
    pl_data = bms_pl_data.objects.get(user_id = cache.get('loggedin_user_id'))
    query_set = bms_pl_booking_history.objects.filter(pl_id = pl_data)
    print(type(query_set))
    if query_set.count() == 0:
        context = {
            "no_data_message":"You do not have any bookings"
        }
        return render(get, "pl-booking-history.html", context)
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
        return render(get, "pl-booking-history.html", context)

def pl_homepage_view(get):
    pl = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
    pl_data = bms_pl_data.objects.get(user_id = pl.user_id)
    total_earning = 0
    query_set = bms_pl_booking_history.objects.filter(pl_id = pl_data.pl_id)
    for booking in query_set:
        total_earning = total_earning + booking.booking_code.total_price_paid
    context = {
        "pl_data" : pl_data,
        "total_earning" : total_earning,
        "total_bookings" : query_set.count(),
        "available_slots" : pl_data.total_slot_count - pl_data.booked_slot_count
    }
    return render(get, "pl-homepage.html",context)

def pl_update_profile(request):
    user_id = cache.get('loggedin_user_id')
    pl_data = bms_pl_data.objects.get(user_id = bms_signup.objects.get(user_id = user_id))
    context = {
        'pl_data' : pl_data,
        'error_message': ''
    }
    if request.method == 'POST':
        manager_name = request.POST.get('manager_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        booking_price = request.POST.get('booking_price')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        email = request.POST.get('email')
        total_slots_count = request.POST.get('total_slots_count')
        description = request.POST.get('description')
        pl_image = request.FILES['pl_image']
        temp = datetime.strptime(opening_time, "%I:%M %p")
        opening_time = datetime.strftime(temp, "%H:%M")
        temp = datetime.strptime(closing_time, "%I:%M %p")
        closing_time = datetime.strftime(temp, "%H:%M")
        new_pl_data = {
            "manager_name": manager_name,
            "address": address,
            "city": city,
            "booking_price": booking_price,
            "opening_time": opening_time,
            "closing_time": closing_time,
            "email": email,
            "total_slot_count": total_slots_count,
            "booked_slot_count": 0,
            "pl_image": pl_image,
            "description": description
        }
        
        if new_pl_data['manager_name'] != pl_data.manager_name:
            pl_data.manager_name = new_pl_data['manager_name']
            pl_data.save()
        if new_pl_data['address'] != pl_data.address:
            pl_data.address = new_pl_data['address']
            pl_data.save()
        if new_pl_data['city'] != pl_data.city:
            pl_data.city = new_pl_data['city']
            pl_data.save()
        if new_pl_data['booking_price'] != pl_data.booking_price:
            pl_data.booking_price = new_pl_data['booking_price']
            pl_data.save()
        if new_pl_data['opening_time'] != pl_data.opening_time:
            pl_data.opening_time = new_pl_data['opening_time']
            pl_data.save()
        if new_pl_data['closing_time'] != pl_data.closing_time:
            pl_data.closing_time = new_pl_data['closing_time']
            pl_data.save()
        if new_pl_data['email'] != pl_data.email:
            pl_data.email = new_pl_data['email']
            pl_data.save()
        if new_pl_data['booked_slot_count'] != pl_data.booked_slot_count:
            pl_data.booked_slot_count = new_pl_data['booked_slot_count']
            pl_data.save()
        if new_pl_data['total_slot_count'] != pl_data.total_slot_count:
            pl_data.total_slot_count = new_pl_data['total_slot_count']
            pl_data.save()
        if new_pl_data['description'] != pl_data.pl_description:
            pl_data.pl_description = new_pl_data['description']
            pl_data.save()
        if new_pl_data['pl_image'] != pl_data.pl_image:
            pl_data.pl_image = new_pl_data['pl_image']
            pl_data.save()
        return redirect(pl_homepage_view)
    return render(request, 'pl-update-profile.html', context)


def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = 'pxyz220@gmail.com'
    msg['from'] = user
    password = 'jnngdekbunxumcno'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def send_sms(phonenumber, sms_content):
    account_sid = 'AC87b7171aff5c77e2cdcedaa8527d4776'
    auth_token = 'a4c9db88ff422a8f863f7ae8a93ac014'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=sms_content,
                                from_='+16616895014',
                                to=phonenumber
                            )
    print(message.sid)

