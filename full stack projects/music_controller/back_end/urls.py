from django.urls import path
from .views import *

urlpatterns = [
    path('api',RoomView.as_view()),
    path('create-room',CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
]