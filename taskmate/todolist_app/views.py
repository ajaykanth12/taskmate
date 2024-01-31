from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import Tasklist

# Create your views here.
def todolist(request):
    all_tasks = Tasklist.objects.all
    #context = {
     #   'welcome_text':"Welcome to Main page todo jinja2"
      #  }
    return render(request,'todolist.html',{'all_tasks': all_tasks})

def contact(request):
    context = {
        'contact_text':"Welcome to contact us"
        }
    return render(request,'contact.html',context)

def about(request):
    context = {
        'about_text':"Welcome to about us"
        }
    return render(request,'about.html',context)
