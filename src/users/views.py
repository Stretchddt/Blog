from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from django.contrib.auth import  login, logout

# Create your views here.
def user_registration(request):
    form = UserRegistration(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users:login') 

    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = UserLogin(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.GET.get('next')) 
            else:
                return redirect('posts:all-posts')

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)

def user_logout(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        return redirect('posts:all-posts')

    context = {
        'user': user
    }

    return render(request, 'users/logout.html', context)