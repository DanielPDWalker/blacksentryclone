from django.contrib.auth import logout
from django.shortcuts import render, redirect


def custom_logout(request):
    logout(request)
    return redirect('index')
