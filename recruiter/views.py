from django.shortcuts import render,HttpResponse
from user.models import Profile
from courses.models import Profile_Course ,Course

# Create your views here.

from courses.models import Course

def home(request):

	courses = Course.objects.all()

	selected = request.GET.getlist('course')

	shortlist = []
	profiles = Profile.objects.all()

	for profile in profiles:
		cnt =0
		for select in selected:
			if(Profile_Course.objects.filter(profile=profile ,course=select).exists() ):
				cnt+=1
		if cnt == len(selected):
			shortlist.append(profile)	
	context = {
		'courses' : courses,
		'shortlist':shortlist
	}
	return render(request , 'recruiter/home.html' , context)

