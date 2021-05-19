from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *

# Create your views.
def index(request):
    send_mail_task.delay(300)
  
    return HttpResponse('celery mail send')
