from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('properties:all'))
    else:
        return render(request, 'home/index.html')
