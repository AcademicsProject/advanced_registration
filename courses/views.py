from django.shortcuts import render,HttpResponse
from .models import Course
from django.db.models import Q
from user.models import Profile

# Create your views here.

def home(request):
    search = request.GET.get('search')

    if search!=None:
        courses = Course.objects.filter( Q(name__icontains = search) | Q(teacher__icontains = search)    )
    else:
        courses = Course.objects.all()

    context={'courses':courses}

    return render(request , 'courses/home.html',context)



def details(request,slug):
    if request.method == 'POST':
        
        profile = Profile.objects.get(user = request.user) 
        if slug in profile.courses:
            return HttpResponse('ERROR') 
        else:
            profile.courses.add(slug)

    context = {'slug':slug}
    return render(request ,'courses/details.html',context )



