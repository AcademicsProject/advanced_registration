from django.shortcuts import render,HttpResponse
from .models import Course,Track,Track_Course
from django.db.models import Q
from user.models import Profile

# Create your views here.

def home(request):
    search = request.GET.get('search')
    trackId = request.GET.get('track')

    courses = Course.objects.all()
    
    if search!=None:
        courses = course.filter( Q(name__icontains = search) | Q(teacher__icontains = search)    )
    
    if trackId!=None:
        track = Track.objects.get(id=trackId)
        track_courses = Track_Course.objects.filter(track=track)
        course_list=[]
        for track_course in track_courses:
            course_list.append(track_course.course.id)

        courses = courses.filter( Q(id__in = course_list)  )

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

def tracks(request):
    tracks = Track.objects.all()
    context = { 'tracks' : tracks }
    return render(request,'courses/tracks.html',context)



