"""chats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import registration_view
from login.views import login_view
from homepage.views import chat_view,addcontact_view,delete_contact,start_chat,sendchar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/register/', registration_view, name="registration"),
    path('', login_view, name="signin"),
    path('chats/', chat_view, name="chats"),
    path('chats/addcontact/', addcontact_view, name="contact"),
    path('chats/contact/delete/<int:id>/', delete_contact, name="delete"),
    path('chats/contact/<int:id>/', start_chat, name="startchat"),
    path('chats/send/', sendchar_view, name="send"),
]
