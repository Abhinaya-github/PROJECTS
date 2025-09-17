from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def viewreceipt(request):
    return render(request,'finance/viewreceipt.html')

def balance(request):
    return render(request,'finance/balance.html' )
