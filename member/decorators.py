from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Profile
from blog.models import Post


def unauthenticated_member(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return function(request, *args, **kwargs)
    return wrap



        
    