from django.shortcuts import render,HttpResponse
from .models import Course,Track,Track_Course,Prerequisite,Profile_Course
from django.db.models import Q
from user.models import Profile

# Create your views here.

def home(request):
    search = request.GET.get('search')
    trackId = request.GET.get('track')

    courses = Course.objects.all()
    
    if search!=None:
        courses = courses.filter( Q(name__icontains = search) | Q(teacher__icontains = search)    )
    
    if trackId!=None:
        track = Track.objects.get(id=trackId)
        track_courses = Track_Course.objects.filter(track=track)
        course_list=[]
        for track_course in track_courses:
            course_list.append(track_course.course.id)

        courses = courses.filter( Q(id__in = course_list)  )

    tracks = Track.objects.all()
    context={'courses':courses , 'tracks':tracks}

    return render(request , 'courses/home.html',context)



def details(request,slug):
    
    course = Course.objects.get(slug=slug)
    eligible = 0 
    
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        course = Course.objects.get(slug=slug)

        if Profile_Course.objects.filter(profile = profile , course=course).exists() :
            return HttpResponse('ERROR ALready enrolled ') 
        else:
            prereq = Prerequisite.objects.filter(course = course).values_list('pre_course',flat=True)
            cleared = Profile_Course.objects.filter(profile=profile , course__in = prereq ,status='C')
            
            prereq = prereq.exclude(pre_course__in = cleared.values_list('course',flat=True) )

            
            if(len(prereq)==0):
                Profile_Course.objects.create(profile=profile , course=course,status='R')

    
        context = {'course':course , 'prereq':prereq  , 'eligible':eligible }
        return render(request ,'courses/details.html',context )

    if request.method == 'GET':
        context = {'course':course}
        return render(request ,'courses/details.html',context )
        

def tracks(request):
    tracks = Track.objects.all()
    context = { 'tracks' : tracks }
    return render(request,'courses/tracks.html',context)



