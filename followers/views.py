from django.shortcuts import render
from .models import Follow

def homepage(request):
    followers = Follow.objects
    return render(request, 'followers/home.html', {'followers': followers})