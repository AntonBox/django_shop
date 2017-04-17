from django.shortcuts import render, redirect
from apps.accounts.forms import CreateUserForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO,
                'You succesfully registered. Please login using your username and password')
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'registration.html', {'form': form})
