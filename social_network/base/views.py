from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/account/logout')
        return render(request, 'base/home.html')
    else:
        return redirect('/account/login')