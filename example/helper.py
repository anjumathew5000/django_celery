from django.core.mail import send_mail


def send_email_without_celery():
    send_mail('CELERYWORKED',"CELERY IS cool",'anju.m@irohub.com',['anjumathew1511@gmail.com'],fail_silently = False)
    return None
