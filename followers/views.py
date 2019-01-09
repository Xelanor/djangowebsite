from django.shortcuts import render, get_object_or_404
from .models import Follow
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def homepage(request):
    followers = Follow.objects
    return render(request, 'followers/home.html', {'followers': followers})

def detail(request, follow_id):
    follow_detail = get_object_or_404(Follow, pk=follow_id)
    return render(request, 'followers/detail.html', {'follow': follow_detail})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'followers/register.html', {'form': form})