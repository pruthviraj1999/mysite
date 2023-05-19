from django.urls import path
from app1 import views



urlpatterns =[
    path ('',views.index),
    path ('sales',views.sales),
    path ('products',views.products),
    path ('users',views.users),
    path ('customers',views.customers)
]