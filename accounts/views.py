from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from game.models import Player

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()


    context = {
        "form": form
    }

    return render(request, 'accounts/register.html', context)