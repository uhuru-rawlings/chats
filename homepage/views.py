from cmath import inf
from http.client import responses
from urllib import response
from django.shortcuts import redirect, render
from authentication.models import Registration
from homepage.models import Contacts,Messages
from django.db.models import Q

# Create your views here.
def chat_view(request):
    user = request.COOKIES['userd']
    if user:
       pass
    else:
        return redirect('signin')
    user = Registration.objects.get(contact = user)
    contacts = Contacts.objects.filter(user = user)
    if contacts:
        chats = ''
        sender = ''
        receiver = ''
        try:
           id = request.COOKIES['chat']
        except:
            # for x in contacts:
            id = contacts[0].id
        if id != 'noid':
            try:
                rchat = Contacts.objects.get(id = id)
                
                if rchat:
                    sender = user
                    receiver = rchat

                    chats = Messages.objects.filter(Q(sender = sender.contact, receiver = receiver.contact) | Q(sender = receiver.contact, receiver = sender.contact))
            except:
                if chats:
                    pass
                else:
                    chats = ''
        else:
            sender = user
            receiver = rchat
            #   nam_sep = ''
            rchat = 'nouser'

        context = {
            'title':'chatapp | Home',
            'contacts':contacts,
            'chats':chats,
            'sender':sender,
            'receiver':receiver
        }
        return render(request,"chart.html",context)
    else:
        contacts = []
        context = {
            'title':'chatapp | Home',
            'contacts':contacts,
            # 'chats':chats,
            # 'sender':sender,
            # 'receiver':receiver
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


def sendchar_view(request):
    if request.method == 'POST':
        try:
            id = request.COOKIES['chat']
            rchat = Contacts.objects.get(id = id)
            if rchat != 'nouser':
                user = request.COOKIES['userd']
                user = Registration.objects.get(contact = user)
                sender = user
                receiver = rchat
                messages = request.POST['messagecontent']

                new_message = Messages(sender = sender.contact, receiver =  receiver.contact, message = messages)
                new_message.save()
                return redirect('/chats/')
        except:
            return redirect('/chats/')
        
  

def logout_view(request):
    user = request.COOKIES['userd']
    if user:
       response = redirect('signin')
       response.delete_cookie("userd")
       return response
    else:
        return redirect('signin')