from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from blog.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  User
from blog.models import UserProfile

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def register(request):
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            return HttpResponseRedirect("/blog/")

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'blog/register.html',
        {'user_form': user_form, 'profile_form': profile_form } )

def auth_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return HttpResponseRedirect('/blog/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'blog/login.html', {})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/')



