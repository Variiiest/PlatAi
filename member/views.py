from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import  UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile 
from django.contrib import messages
from .decorators import unauthenticated_member
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib	import	messages
from django.views.generic import ListView

@login_required
def edit(request):
    if request.method=='POST':
        profile_form= ProfileEditForm(instance= request.user.profile, data= request.POST, files= request.FILES)
        user_form= UserEditForm(instance= request.user, data=request.POST)
        if profile_form.is_valid() and user_form.is_valid:
            profile_form.save()
            user_form.save()
            messages.success(request,'Profile updated	successfully')	
        else:
            messages.error(request, 'Error updating profile.')
    else:
        profile_form= ProfileEditForm(instance= request.user.profile)
        user_form= UserEditForm(instance= request.user)
    return render(request, 'account/edit.html', {'profile_form':profile_form, 'user_form':user_form})

               
   
@unauthenticated_member           
def register(request):
    if request.method== 'POST':
        user_form= UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user= new_user)
            return render(request, 'account/register_done.html', {'new_user':new_user})
        
    else:
        user_form= UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})
    
        


@login_required 
def login_success(request): 
    return redirect("profile")


    
def profile(request,username):
    user= User.objects.get(username=username)
    id_= user.id
    posts= user.blog_posts.all()
    profile= Profile.objects.get(pk=id_)
    return render(request, 'profile/profile.html',{'profile':profile, 'posts':posts})








    