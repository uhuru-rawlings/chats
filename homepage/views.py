from django.shortcuts import redirect, render
from authentication.models import Registration
from homepage.models import Contacts,Messages

# Create your views here.
def chat_view(request):
    user = request.COOKIES['userd']
    if user:
        if request.method == 'POST':
            pass
    else:
        return redirect('signin')
    context = {
        'title':'chatapp | login',
    }
    return render(request,"chart.html",context)


def addcontact_view(request):
    user = request.COOKIES['userd']
    if user:
        if request.method == 'POST':
            contactname = request.POST['']
            contact = request.POST['']
            user = Registration.objects.get(contact = user)
            check_contact = Contacts.objects.filter(user = user,contact = contact)
            if check_contact.exists():
                error = 'user with these details already exist.'
                return redirect('/chats/')
            else:
                new_user = Contacts(user = user, contactname = contactname, contact = contact)
                new_user.save()
                return redirect('/chats/')
    else:
        return redirect('signin')