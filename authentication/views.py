from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import Registration

# Create your views here.
def registration_view(request):
    error = ''
    success = ''
    if request.method == 'POST':
        username = request.POST['username']
        contact = request.POST['contacts']
        userimage = request.POST['userimage']
        password = request.POST['passwords']

        check_contact = Registration.objects.filter(contact = contact)
        if check_contact.exists():
            error = 'user with these details already exist.'
        else:
            new_user = Registration(username = username,contact = contact,userimage = userimage, password = make_password(password))
            new_user.save()
            success = 'user created successfully. go to <a href={% url "signin" %}>login</a>'
    context = {
        'title':'chatapp | register',
        'error':error,
        'success':success
    }
    return render(request,"register.html",context)

def login_view(request):
    context = {
        'title':'chatapp | login',
    }
    return render(request,"login.html",context)