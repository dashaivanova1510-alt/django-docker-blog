from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            author_group = Group.objects.get(name='author')
            user.groups.add(author_group)
            login(request, user)
            return redirect('home') # Перенаправляємо на головну
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})