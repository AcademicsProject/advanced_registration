from django.shortcuts import render,HttpResponse
from .models import Course
from django.db.models import Q

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
    
    # course = request.objects.filter(slug=slug).first()
    context={'slug':slug}
    return render(request ,'courses/details.html',context )

