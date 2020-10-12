from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import *
from .forms import CreatePostForm,EditProfileForm

# Create your views here.
@login_required(login_url='login')
def Home(request):
    form = CreatePostForm()
    if request.method ==  'POST':
        form = CreatePostForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user= request.user
            instance.save()
            form = CreatePostForm()
    post = Post.objects.all().order_by('-time')




    return render(request,'insta/post_list.html',{'posts':post,'form':form})
@unauthenticated_user
def Login(request):

    if request.method == 'POST':
       username= request.POST.get('username')
       password= request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('home')

       else:
           messages.info(request,'USERNAME or PASSWORD is incorrect')



    return render(request,'insta/login.html',{})

def Logout(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def Register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'Account was created successfully for'+user)
            return redirect('login')
    return render(request,'insta/register.html',{'form':form})


@login_required(login_url='login')
def Like(request,id):
    user = request.user
    print(user)
    post = Post.objects.get(id=id)
    like = Likes.objects.create(user=user,post=post)

    like.save()
    Like =Likes.objects.all().count()
    print (like)


    return redirect('home')

@login_required(login_url='login')
def Profile(request):
    user= request.user
    post = user.post_set.all().order_by('-time')
    return render(request,'insta/profile.html',{'user_post':post})

@login_required(login_url='login')
def EditProfile(request):
    user =request.user
    form = EditProfileForm()
    
    if request.method == 'POST':
        if form.is_valid:
            form = EditProfileForm(request.POST)
            form.save()
            return redirect('profile')
    return render(request,'insta/add-profile.html',{'form':form})
