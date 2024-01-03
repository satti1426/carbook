from users.models import *

def my_cron_job():
    User.objects.create(email='a@gmail.com')
    return None