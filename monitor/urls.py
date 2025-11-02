from django.urls import path
from .views import DriverListCreateView,BusListCreateView,DrowsinessEventListCreateView

urlpatterns=[
    path('drivers/',DriverListCreateView.as_view()),
    path('buses/',BusListCreateView.as_view()),
    path('events/',DrowsinessEventListCreateView.as_view())


]