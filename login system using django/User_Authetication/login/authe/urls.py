from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signOut"),
    path('activate/<uidb64>/<tokens>',views.activate,name="activate"),
]