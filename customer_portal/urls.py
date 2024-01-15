from django.urls import path, include
from .views import index, login, auth_view, logout_view, register, registration, search, search_results, rent_vehicle, confirm, manage, update_order, delete_order

urlpatterns = [
    path('index/', index),
    path('login/', login),
    path('auth/', auth_view),
    path('logout/', logout_view),
    path('register/', register),
    path('registration/', registration),
    path('search/', search),
    path('search_results/', search_results),
    path('rent/', rent_vehicle),
    path('confirmed/', confirm),
    path('manage/', manage),
    path('update/', update_order),
    path('delete/', delete_order),
]
