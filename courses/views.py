from django.shortcuts import render
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