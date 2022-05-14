from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import Registration


# Create your views here.
def login_view(request):
    error = ''
    success = ''
    if request.method == 'POST':
        contact = request.POST['contact']
        password = request.POST['password']

        getuser = Registration.objects.filter(contact = contact)
        if getuser.exists():
            user = Registration.objects.get(contact = contact)
            if check_password(password, user.password):
                response = redirect('/chats/')
                response.set_cookie("userd",contact)
                return response
            else:
                error = 'Wrong password, try again.'
        else:
            error = 'Wrong details provided. check and try again.'
    context = {
        'title':'chatapp | login',
        'error':error,
        'success':success
    }
    return render(request,"login.html",context)