from http.client import responses
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
    try:
      id = request.COOKIES['chat']
      rchat = Contacts.objects.get(id = id)
    except:
      rchat = 'nouser'
    user = Registration.objects.get(contact = user)
    contacts = Contacts.objects.filter(user = user)
    context = {
        'title':'chatapp | Home',
        'contacts':contacts,
        'rchat':rchat
    }
    return render(request,"chart.html",context)


def addcontact_view(request):
    user = request.COOKIES['userd']
    if user:
        if request.method == 'POST':
            contactname = request.POST['contactname']
            contact = request.POST['phonenumber']
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

def delete_contact(request, id):
    contact = Contacts.objects.get(id = id)
    contact.delete()
    return redirect('/chats/')


def start_chat(request, id):
    response = redirect('/chats/')
    response.set_cookie("chat",id)
    return response
  