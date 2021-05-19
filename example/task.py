from celery import shared_task
# from celery.task.shedules import crontab
# from celery.decorators import periodic_task
from time import sleep 
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task(duration):
    sleep(duration)
    send_mail('CELERYWORKED',"CELERY IS COOL",'anju.m@irohub.com',['anjumathew1511@gmail.com'],fail_silently = False)
    return None
