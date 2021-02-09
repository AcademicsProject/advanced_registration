from django.db import models
from django.contrib.auth.models import User
from user.models import Profile

# Create your models here.

class Course(models.Model):
    id = models.CharField(max_length=5 , primary_key=True)
    name = models.CharField(max_length=100)
    stream = models.CharField(max_length=32)
    strength = models.IntegerField()
    description = models.CharField(max_length=255)
    teacher = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    relation = models.ManyToManyField(
        Profile,
        through='Profile_Course',
        through_fields=( 'course','profile')
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Track(models.Model):
    name=models.CharField(max_length=50 ,default=None )
    id = models.CharField(max_length=5,unique=True,primary_key=True)

    relation = models.ManyToManyField(
        Course,
        through='Track_Course',
        through_fields=('track','course' )
    )

    def __str__(self):
        return self.name

    
class Profile_Course(models.Model):

    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    course = models.ForeignKey(Course ,on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.name+" is enrolled in "+self.course.name

class Track_Course(models.Model):
    track = models.ForeignKey(Track , on_delete=models.CASCADE)
    course= models.ForeignKey(Course ,on_delete=models.CASCADE)

    def __str__(self):
        return self.track.name+" has a course on "+self.course.name

