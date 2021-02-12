from django.shortcuts import render,HttpResponse

# Create your views here.

from courses.models import Course

def home(request):

	courses = Course.objects.all()

	if request.method == 'POST':
		selected = request.POST.get('selected')
	
	if selected is None:
		shortlist = Profile.objects.all()
	else:
		shortlist = Profile_Course.objects.filter(course__in = selected).values_list( roll ,flat=True)
		shortlist = Profile.objects.filter( __in = shortlist )
	
	context = {
		'courses' : courses
		'shortlist':shortlist
	}
	return render(request , 'recruiter/home.html' , context)

