from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}! Your Account has been created. You can now log in.')
            return redirect('songs:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
