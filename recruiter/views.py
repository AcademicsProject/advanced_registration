from django.shortcuts import render,HttpResponse

# Create your views here.

from courses.models import Course

def home(request):

	courses = Course.objects.all()

	if request.method == "POST" :
		print(request.POST)

	context = {
		'courses' : courses
	}
	return render(request , 'recruiter/home.html' , context)

