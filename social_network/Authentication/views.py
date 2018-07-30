from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def REGISTER(request):
    if request.user.is_superuser:
        return redirect('/account/logout')
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/account/login')
        else:
            form = UserCreationForm()
        return render(request, 'Authentication/register.html', {'form':form})
    else:
        return HttpResponse('You are already logged in')

def LOGIN(request):
    if request.user.is_superuser:
        return redirect('/account/logout')
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None and not user.is_superuser:
                    login(request,user)
                    return redirect('/')
            else:
                return HttpResponse('<h1>404 Error</h1>')
        else:
            form = AuthenticationForm()
        return render(request,'Authentication/login.html', {'form':form})
    else:
        return HttpResponse('You are already logged in')
    
def LOGOUT(request):
    logout(request)
    return redirect('/account/login')