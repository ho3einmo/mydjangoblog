from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect('Blogs:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            auth_login(request, user)
            return redirect('Blogs:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('Blogs:list')
    return render(request, 'accounts/logout.html')  # Render a confirmation page or similar