import time
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Hi suchi")

def date(request):
    time.sleep(10)
    return HttpResponse(f'Current Time is: {datetime.now()}')   


def about(request):
    return HttpResponse('hi team')