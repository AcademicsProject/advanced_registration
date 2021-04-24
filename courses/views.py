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
    
    if request.user.is_authenticated==0:
        return HttpResponse("Please Login First")

    course = Course.objects.get(slug=slug)
    eligible = 'N' 
    profile = Profile.objects.get(user = request.user)
    
    prereq = Prerequisite.objects.filter(course = course).values_list('pre_course',flat=True)
    
    cleared = Profile_Course.objects.filter(profile=profile  ,status='C').values_list('course',flat=True)
    current = Profile_Course.objects.filter(profile=profile ,status='R').values_list('course',flat=True)

    #print(profile)

    
    cleared = Course.objects.filter(id__in = cleared).values_list('id',flat=True)
    current = Course.objects.filter(id__in = current)


    prereq_list = []
    cleared_list = []
    for pre in prereq:
        if pre in cleared :
            cleared_list.append(pre)
        else:
            prereq_list.append(pre)

     
    if course.id in cleared:
        eligible='C'
    elif course.id in current:
        eligible='R'
    elif len(prereq_list)==0:
        eligible='A'
    
    if request.method == 'POST':    
        if(len(prereq_list)==0):
            Profile_Course.objects.create(profile=profile , course=course,status='R')
            eligible='R'

    prereq = Course.objects.filter(id__in = prereq_list)
    cleared = Course.objects.filter(id__in = cleared_list)
    #print(prereq,cleared)
    context = { 'course':course  ,'eligible' :eligible ,'prereq':prereq ,'cleared':cleared}    
    return render(request ,'courses/details.html',context )
        

def tracks(request):
    tracks = Track.objects.all()
    context = { 'tracks' : tracks }
    return render(request,'courses/tracks.html',context)


