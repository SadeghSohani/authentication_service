from django.contrib import admin
from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('user', UserViewSet.as_view({
        'get' : 'list',
        'post' : 'create'
    })),
    path('user/auth', UserViewSet.as_view({
        'post' : 'authenticate_user'
    })),   
    path('user/reserve', UserViewSet.as_view({
        'post' : 'reserve_flight'
    })), 
    path('user/panel', UserViewSet.as_view({
        'get' : 'user_panel'
    })),   
]


