from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
             login(request, user)
             return redirect('primary/')
        else:
             return HttpResponse('Hello;/')
    else:
        return render(request,'index.html')
    
def primary(request):
    return render(request,'primary.html')