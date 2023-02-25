from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def sign_up(request):
    template_name = 'auth_app/signup.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context = {'form': form}
    return render(request, template_name, context)


def login_view(request):
    template_name = 'auth_app/login.html'
    if request.method == 'POST':
        user1 = request.POST['un']
        pass1 = request.POST['pw']
        user = authenticate(username=user1, password=pass1)
        if user:
            login(request, user)
            return redirect('all_order_url')
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('login_url')
