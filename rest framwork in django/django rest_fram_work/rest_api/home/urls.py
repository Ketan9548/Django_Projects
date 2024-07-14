from django.urls import path , include
from home import views


urlpatterns = [
    path('',views.home,name="home"),
    path('post_todo',views.post_todo,name="post_todo"),
]
