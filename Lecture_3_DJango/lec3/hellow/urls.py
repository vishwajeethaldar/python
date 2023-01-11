from django.urls import path
from . import views

urlpatterns  = [
    path("", views.index, name="index"),
    path("honey", views.honey, name="honey"),
    path("home", views.home, name="home"),
    path("home/<str:name>", views.greet, name="greet"),
   
]

