from typing import Any
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help='run to adduser'

    def handle(self, *args, **options):
     adduser = User.objects.bulk_create(
         [ 
          User(first_name='kiran',username='kiran@gmail.com',email='kiran@gmail.com'),
          User(first_name='prabh',username='prabh@gmail.com',email='prabh@gmail.com'),
          User(first_name='karan',username='karan@gmail.com',email='karan@gmail.com'),
          User(first_name='manleen',username='manleen@gmail.com',email='manleen@gmail.com'),
          ] 
     )
     self.stdout.write(f"created user" ["first_name"])
 