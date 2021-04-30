from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import HomeNotification


def home(request):
    # Get all active HomeNotifications and send them to the homepage template
    notifications = HomeNotification.objects.all().filter(active=True)
    context = {'notifications': notifications}

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/accounts/login/?next=/')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'sign_up.html', {'form': f})