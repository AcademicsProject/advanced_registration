from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user= User.objects.create_user(roll,email,password)
        customUser =CustomUser(name=name)
        customUser.save()
        return HttpResponse('SUCCESS')

    else:
        return HttpResponse('ERROR')


def login_fn(requesst):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        password = request.POST.get('password')
        return HttpResponse('SUCCESS')
    else:
        return HttpResponse('ERROR')


def logout_fn(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return HttpResponse('ERROR')










