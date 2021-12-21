from django.shortcuts import render, redirect
import requests
from .forms import signupform, loginform
from parking_lots.views import register_pl_view, pl_homepage_view
from parking_lots.models import bms_pl_data
from admin_panel.views import admin_homepage_view
from .models import bms_signup
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from django.contrib.auth.hashers import check_password, make_password
from bms_customer_transactions.models import bms_cu_booking_history, bms_cu_faviorate
# Create your views here.

#pure django form rendering
# def signup_view(requests):
#     signup_data = signupform()
#     if requests.method == "POST":
#         signup_data = signupform(requests.POST or None)
#         if signup_data.is_valid():
#             #print(signup_data.cleaned_data)
#             try:
#                 bms_user = bms_signup.objects.get(username = signup_data.cleaned_data['username'])
#                 if bms_user.username == signup_data.cleaned_data['username']:
#                     context = {
#                         "signup_form" : signup_data,
#                         'error_message' : "Username already exists"
#                     }
#                     return render(requests, "signup-page.html", context)
#                 elif bms_user.phonenumber == signup_data.cleaned_data['phonenumber']:
#                     context = {
#                         "signup_form" : signup_data,
#                         'error_message' : "User with this phonenumber already exists"
#                     }
#                     return render(requests, "signup-page.html", context)
#             except ObjectDoesNotExist:
#                 if signup_data.cleaned_data['password'] != signup_data.cleaned_data['confirm_password']:
#                     context = {
#                         'signup_form': signup_data,
#                         'error_message' : "Please enter same passwords"
#                     }
#                     return render(requests, "signup-page.html", context)
#                 signup_data.cleaned_data['user_type'] = 1
#                 signup_data.cleaned_data['password'] = make_password(signup_data.cleaned_data['password'])
#                 del signup_data.cleaned_data['confirm_password']
#                 #print(signup_data.cleaned_data)
#                 bms_signup.objects.create(**signup_data.cleaned_data)
#             return render(requests, "customer-homepage.html")
#         else:
#             print(signup_data.errors)
#     context = {
#         "signup_form" : signup_data,
#         'error_message': ''
#     }
#     return render(requests, "signup-page.html", context)

#2nd template vaibhav design
def signup_view(request):
    if request.method == "POST":
        #print(signup_data.cleaned_data)
        username = request.POST.get('username')
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('create_password')
        confirm_password = request.POST.get('confirm_password')
        signup_data = {
            "name": name,
            "username": username,
            "phonenumber" : phonenumber,
            "password": password
        }
        try:
            bms_user = bms_signup.objects.get(username = username)
            if bms_user.username == username:
                context = {
                    'error_message' : "Username already exists"
                }
                return render(request, "customer-signup.html", context)
            elif bms_user.phonenumber == phonenumber:
                context = {
                    'error_message' : "User with this phonenumber already exists"
                }
                return render(request, "customer-signup.html", context)
        except ObjectDoesNotExist:
            if password != confirm_password:
                context = {
                    'error_message' : "Please enter same passwords"
                }
                return render(request, "customer-signup.html", context)
            signup_data['user_type'] = 1
            signup_data['password'] = make_password(password)
            #print(signup_data.cleaned_data)
            user_id = bms_signup.objects.create(**signup_data).user_id
            cache.set('loggedin_user_id', user_id)
        return render(request, "customer-homepage.html")
    context = {
        'error_message': ''
    }
    return render(request, "customer-signup.html", context)


#pure django form
# def pl_signup_view(requests):
#     signup_data = signupform()
#     if requests.method == "POST":
#         signup_data = signupform(requests.POST or None)
#         if signup_data.is_valid():
#             #print(signup_data.cleaned_data)
#             try:
#                 bms_user = bms_signup.objects.get(username = signup_data.cleaned_data['username'])
#                 if bms_user.username == signup_data.cleaned_data['username']:
#                     context = {
#                         "signup_form" : signup_data,
#                         'error_message' : "Username already exists"
#                     }
#                     return render(requests, "signup-page.html", context)
#                 elif bms_user.phonenumber == signup_data.cleaned_data['phonenumber']:
#                     context = {
#                         "signup_form" : signup_data,
#                         'error_message' : "User with this phonenumber already exists"
#                     }
#                     return render(requests, "signup-page.html", context)
#             except ObjectDoesNotExist:
#                 if signup_data.cleaned_data['password'] != signup_data.cleaned_data['confirm_password']:
#                     context = {
#                         'signup_form': signup_data,
#                         'error_message' : "Please enter same passwords"
#                     }
#                     return render(requests, "signup-page.html", context)
#                 signup_data.cleaned_data['user_type'] = 2
#                 signup_data.cleaned_data['password'] = make_password(signup_data.cleaned_data['password'])
#                 del signup_data.cleaned_data['confirm_password']
#                 #print(signup_data.cleaned_data)
#                 bms_signup.objects.create(**signup_data.cleaned_data)
#                 usr_id = bms_signup.objects.get(username = signup_data.cleaned_data['username']).user_id
#                 cache.set('user_id', usr_id)
#             return redirect(register_pl_view)
#         else:
#             print(signup_data.errors)
#     context = {
#         "signup_form" : signup_data,
#         'error_message': ''
#     }
#     return render(requests, "signup-page.html", context)


#2nd template vaibhav design
def pl_signup_view(requests):
    if requests.method == "POST":
        #print(signup_data.cleaned_data)
        username = requests.POST.get('username')
        name = requests.POST.get('name')
        phonenumber = requests.POST.get('phonenumber')
        password = requests.POST.get('password')
        confirm_password = requests.POST.get('confirm_password')
        signup_data = {
            "name": name,
            "username": username,
            "phonenumber" : phonenumber,
            "password": password
        }
        try:
            bms_user = bms_signup.objects.get(username = username)
            if bms_user.username == username:
                context = {
                    'error_message' : "Username already exists"
                }
                return render(requests, "pl-signup.html", context)
            elif bms_user.phonenumber == phonenumber:
                context = {
                    'error_message' : "User with this phonenumber already exists"
                }
                return render(requests, "pl-signup.html", context)
        except ObjectDoesNotExist:
            if password != confirm_password:
                context = {
                    'error_message' : "Please enter same passwords"
                }
                return render(requests, "pl-signup.html", context)
            signup_data['user_type'] = 2
            print(signup_data['password'])
            print(password)
            signup_data['password'] = make_password(password)
            print(signup_data['password'])
            #print(signup_data.cleaned_data)
            user_id = bms_signup.objects.create(**signup_data).user_id
            cache.set('loggedin_user_id', user_id)
        return redirect(register_pl_view)
    context = {
        'error_message': ''
    }
    return render(requests, "pl-signup.html", context)

#pure django form
# def login_view(requests):
#     login_data = loginform()
#     if requests.method == "POST":
#         login_data = loginform(requests.POST or None)
#         if login_data.is_valid():
#             try:
#                 bms_user = bms_signup.objects.get(username = login_data.cleaned_data['username'])
#                 if not check_password(login_data.cleaned_data['password'], bms_user.password):
#                     context = {
#                         'login_form' : login_data,
#                         'error_message' : "Incorrect Password"
#                     }
#                     return render(requests, "login-page.html", context)
#                 cache.set('loggedin_user_id', bms_user.user_id)
#                 if bms_user.user_type == 1:
#                     return redirect(customer_homepage_view)
#                 else:
#                     return redirect(pl_homepage_view)
#             except ObjectDoesNotExist:
#                 context = {
#                     'login_form': login_data,
#                     'error_message': "User Does Not Exist"
#                 }
#                 return render(requests, "login-page.html", context)   
#         else:
#             print(login_data.errors)
#     context = {
#         'login_form': login_data,
#         'error_message': ''
#     }
#     return render(requests, 'login-page.html', context)

#2nd-login-webpage-vaibhav
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            bms_user = bms_signup.objects.get(username = username)
            if not check_password(password, bms_user.password):
                context = {
                    'error_message' : "Incorrect Password"
                }
                return render(request, "login.html", context)
            cache.set('loggedin_user_id', bms_user.user_id)
            if bms_user.user_type == 1:
                return redirect(customer_homepage_view)
            elif bms_user.user_type == 2:
                return redirect(pl_homepage_view)
            else:
                return redirect(admin_homepage_view)
        except ObjectDoesNotExist:
            context = {
                'error_message': "User Does Not Exist"
            }
            return render(request, "login.html", context)   
    context = {
        'error_message': ''
    }
    return render(request, 'login.html', context)

def update_profile_view(request):
    user_data = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
    context = {
        'user_data' : user_data,
        'error_message': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        try:
            bms_user = bms_signup.objects.get(username = username)
            if bms_user.user_id != user_data.user_id:
                context = {
                    'error_message' : "Username already exists",
                    'user_data' : user_data
                }
                return render(request, "user-profile-update.html", context)
            else:
                try:
                    bms_user = bms_signup.objects.get(phonenumber = phonenumber)
                    if bms_user.user_id != user_data.user_id:
                        context = {
                            'error_message' : "User with this phonenumber already exists",
                            'user_data' : user_data
                        }
                        return render(request, "user-profile-update.html", context)
                except ObjectDoesNotExist:
                    if phonenumber != user_data.phonenumber:
                        user_data.phonenumber = phonenumber
                        user_data.save()
        except ObjectDoesNotExist:
            if user_data.username != username:
                user_data.username = username
                user_data.save()
        if name != user_data.name:
            user_data.name = name
            user_data.save()
        if user_data.user_type == 1:
            return redirect(customer_homepage_view)
        elif user_data.user_type == 2:
            return redirect(pl_homepage_view)
    return render(request, 'user-profile-update.html', context)

def verify_password_view(request):
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        bms_user = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
        if not check_password(current_password, bms_user.password):
            context = {
                'error_message' : "Incorrect pasword"
            }
            return render(request, "verify-old-password.html", context)
        return redirect(change_password_view)
    context = {
        'error_message': ''
    }
    return render(request, 'verify-old-password.html', context)

def change_password_view(request):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        bms_user = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
        if new_password != confirm_password:
            context = {
                'error_message' : "Please enter same paswords"
            }
            return render(request, "change-password.html", context)
        else:
            bms_user.password = make_password(new_password)
            bms_user.save()
            if bms_user.user_type == 1:
                return redirect(customer_homepage_view)
            elif bms_user.user_type == 2:
                return redirect(pl_homepage_view)
            else:
                return redirect(admin_homepage_view)
    context = {
        'error_message': ''
    }
    return render(request, 'change-password.html', context)

def homepage_view(request):
    if request.method == "POST":
        city = request.POST.get('city')
        address = request.POST.get('place_address')
        queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
        result_count = queryset.count()
        print("count=" + str(result_count))
        if result_count == 0:
            context = {
                'no_data_message': 'No Parking Lots Near "' + address + '" in "' + city + '"'
            }
        else:
            context = {
                'parking_lots':queryset
            }
        return render(request, "parking-lots.html", context)
    return render(request, "homepage.html")
    
def customer_homepage_view(request):
    user = bms_signup.objects.get(user_id = cache.get('loggedin_user_id'))
    fav_query_set = bms_cu_faviorate.objects.filter(user_id = user)
    recent_book_query_set = bms_cu_booking_history.objects.filter(user_id = user)[:5]
    context = {
        "fav_pl": fav_query_set,
        "recent_book" : recent_book_query_set
    }
    if request.method == "POST":
        city = request.POST.get('city')
        address = request.POST.get('place_address')
        if "search_button" in request.POST:
            
            queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
            result_count = queryset.count()
            print("count=" + str(result_count))
            if result_count == 0:
                context = {
                    'no_data_message': 'No Parking Lots Near "' + address + '" in "' + city + '"'
                }
                return render(request, "parking-lots.html", context)
            else:
                queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
                context = {
                            "parking_lots" : queryset,
                            "city" : city,
                            "address" : address,
                            'no_data_message': '',
                        }
                return render(request, "parking-lots.html", context)
        elif "sort_button" in request.POST:
            sort_type = request.POST.get('sort')
            if sort_type == 'price_high':
                queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('-booking_price')
                context = {
                    "parking_lots" : queryset,
                    "city" : city,
                    "address" : address
                }
            elif sort_type == 'price_low':
                queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('booking_price')
                context = {
                        "parking_lots" : queryset,
                        "city" : city,
                        "address" : address
                }
            else:
                queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
                context = {
                        "parking_lots" : queryset,
                        "city" : city,
                        "address" : address
                }
            return render(request, "parking-lots.html", context)
    return render(request, "customer-homepage.html", context)

# def customer_homepage_view(request):
#     if request.method == "GET":
#         city = request.GET.get('city', "")
#         address = request.GET.get('place_address', "")
        
#         sort = request.GET.get('sort', "")
#         sort_status = request.GET.get('sort-button', "")
#         print(city)
#         print(address)
#         if sort == 'price_high':
#             queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('-booking_price')
#             context = {
#                 "parking_lots" : queryset
#             }
#         elif sort == 'price_low':
#             queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('booking_price')
#             context = {
#                 "parking_lots" : queryset
#             }
#         else:
#             queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
#             context = {
#                 "parking_lots" : queryset
#             }
#         return render(request, "parking-lots.html", context)
#     return render(request, "customer-homepage.html")
    
# def search_result(request):
#     city = request.GET.get('city')
#     address = request.GET.get('place_address')
    
#     sort = request.GET.get('sort')
#     sort_status = request.GET.get('sort-button')
#     print(city)
#     print(address)
#     if sort == 'price_high':
#         queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('-booking_price')
#         context = {
#             "parking_lots" : queryset
#         }
#     elif sort == 'price_low':
#         queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address).order_by('booking_price')
#         context = {
#             "parking_lots" : queryset
#         }
#     else:
#         queryset = bms_pl_data.objects.filter(city__icontains=city).filter(address__icontains=address)
#         context = {
#             "parking_lots" : queryset
#         }
#     return render(request, "parking-lots.html", context)

