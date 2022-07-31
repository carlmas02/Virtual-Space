from django.contrib import admin
from django.urls import path,include

from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/',getToken),
    path('',lobby,name = 'lobby'),
    path('room/',room,name = 'room'),
    path('sign-up/',signup,name = 'signup'),
    path('setup/',settings,name = 'setup'),
    path('create-room/',create,name = 'create-room'),

]
