from django.urls import path
from app1 import views



urlpatterns =[
    path ('',views.index),
    path ('sales',views.sales),
    path ('product2',views.product2),
]