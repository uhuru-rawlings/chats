from django.shortcuts import render

# Create your views here.
def chat_view(request):
    context = {
        'title':'chatapp | login',
    }
    return render(request,"chart.html",context)