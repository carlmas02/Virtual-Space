from django.contrib import admin
from django.urls import path,include

from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_user),
    path('get-token/',getToken),
    path('',lobby,name = 'lobby'),
    path('room/',room,name = 'room'),
    path('sign-up/',signup,name = 'signup'),
    path('setup/',settings,name = 'setup'),
    path('create-room/',create,name = 'create-room'),
    path('validate-room/',validate_room,name = 'validate-room'),
    path('room-user/',room_user,name = 'users-room'),
    path('addmsg',addmsg,name='addmsg'),
    path('getmsg',getmsg,name='getmsg')
]








