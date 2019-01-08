from django.shortcuts import render, get_object_or_404
from .models import Follow

def homepage(request):
    followers = Follow.objects
    return render(request, 'followers/home.html', {'followers': followers})

def detail(request, follow_id):
    follow_detail = get_object_or_404(Follow, pk=follow_id)
    return render(request, 'followers/detail.html', {'follow': follow_detail})