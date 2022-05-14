from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import Registration

# Create your views here.
def registration_view(request):
    context = {
        'title':'chatapp | register',
    }
    return render(request,"register.html",context)

def login_view(request):
    context = {
        'title':'chatapp | login',
    }
    return render(request,"login.html",context)