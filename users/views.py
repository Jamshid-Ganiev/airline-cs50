
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)

    return render(request, "users/login.html", {
        "message": "Logged Out"
    })

def signup_view(request):
    pass