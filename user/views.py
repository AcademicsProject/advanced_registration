from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Profile

# Create your views here.

def home(request):
    return render(request , 'user/index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        user= User.objects.create_user(roll,email,password)
        profile =Profile(name=name)
        profile.save()
        return redirect('/')
    else:
        return render(request , 'user/login.html')

        


def login_fn(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        password = request.POST.get('password')

        user = authenticate(username=roll , password=password )

        if user is not None:
            login(request,user)
           
            return redirect('/')

        else:
            return HttpResponse('No user found')

    else:
        return render(request , 'user/login.html')

        
def logout_fn(request):
    
    logout(request)
    return redirect('/')
    









