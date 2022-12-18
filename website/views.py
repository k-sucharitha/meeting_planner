import time
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings. models import Meeting

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html', context={'num_meetings':Meeting.objects.count()})

    
def date(request):
    time.sleep(10)
    return render(request, '', context={})


def about(request):
    return render(request, '', context={})