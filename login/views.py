from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import Registration


# Create your views here.
def login_view(request):
    error = ''
    success = ''
    if request.method == 'POST':
        contact = request.POST['contact']
        password = request.POST['password']
    context = {
        'title':'chatapp | login',
        'error':error,
        'success':success
    }
    return render(request,"login.html",context)