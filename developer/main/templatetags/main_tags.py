from django import template



from ..models import *

register = template.Library()

@register.simple_tag
def get_profiles():
    return Profile.objects.all()
@register.simple_tag
def get_friends():

    friends = Friend.objects.all()

    return friends