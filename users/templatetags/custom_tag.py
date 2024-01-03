from django import template
from django import template
from users.models import *

register = template.Library()

print('11111111111111')

@register.filter(name='total_users')
def total_users(value):
    return User.objects.all().count()
   
  
@register.simple_tag
def tag_name(arg1, arg2, arg3):
   print(arg1)
   print(arg2)
   return "hello"
