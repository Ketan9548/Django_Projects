# your_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# @login_required
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
# @login_required
def user_logout(request):
    logout(request)
    return redirect('login')