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
    context={'courses':courses , 'tracks':tracks , 'trackId' : trackId}

    return render(request , 'courses/home.html',context)



def details(request,slug):
    
    course = Course.objects.get(slug=slug)
    eligible = 'N' 
    profile = Profile.objects.get(user = request.user)
    
    prereq = Prerequisite.objects.filter(course = course).values_list('pre_course',flat=True)
    
    cleared = Profile_Course.objects.filter(profile=profile  ,status='C').values_list('course',flat=True)
    current = Profile_Course.objects.filter(profile=profile ,status='R').values_list('course',flat=True)
    
    cleared = Course.objects.filter(id__in = cleared)
    current = Course.objects.filter(id__in = current)

    cleared_p = cleared.filter(course__in = prereq)
    prereq = prereq.exclude(pre_course__in = cleared_p )


    if course in cleared:
        eligible='C'
    elif course in current:
        eligible='R'
    elif len(prereq)==0:
        eligible='A'
    
    if request.method == 'POST':    
        if(len(prereq)==0):
            Profile_Course.objects.create(profile=profile , course=course,status='R')

    context = { 'course':course  ,'eligible' :eligible ,'prereq':prereq ,'cleared':cleared_p}    
    return render(request ,'courses/details.html',context )
        

def tracks(request):
    tracks = Track.objects.all()
    context = { 'tracks' : tracks }
    return render(request,'courses/tracks.html',context)



