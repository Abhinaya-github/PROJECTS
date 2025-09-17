from django.urls import path
from . import views

urlpatterns=[
    path('receipt/',views.viewreceipt,name='receipt'),
    path('balance/',views.balance,name='balance'),
]