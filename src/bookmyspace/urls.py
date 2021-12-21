"""bookmyspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from login.views import add_new_user, homepage
#from accounts.views import login_view, signup_view, logout_view, home_view
from bms_users.views import pl_signup_view, signup_view, login_view, homepage_view, customer_homepage_view, update_profile_view, verify_password_view, change_password_view
from parking_lots.views import register_pl_view, parking_lot_detail_view, pl_homepage_view, pl_booking_history_view, pl_update_profile
from bms_customer_transactions.views import booking_history_view, fav_pl_view
from admin_panel.views import admin_homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('signup/', signup_view),
    path('signup-pl', pl_signup_view),
    path('login', login_view),
    path('cus-homepage',customer_homepage_view, name="cus-homepage"),
    path('pl-homepage', pl_homepage_view),
    path('register-pl', register_pl_view),
    path('pl/<int:pl_id>/', parking_lot_detail_view, name="parking-lot-details"),
    path('cu-bh/', booking_history_view),
    path('pl-bh/',pl_booking_history_view),
    path('bms-admin-panel/', admin_homepage_view),
    path('vp/', verify_password_view),
    path('chp/', change_password_view),
    path('pl-up/', pl_update_profile),
    path('up/', update_profile_view),
    path('fav/', fav_pl_view)
    # path('logout', logout_view),
    # path('homepage', home_view),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
