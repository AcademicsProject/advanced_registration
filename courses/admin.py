from django.contrib import admin
from .models import Course,Track,Profile_Course,Track_Course , Prerequisite

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('id',)} # new

admin.site.register(Course, CourseAdmin)
admin.site.register(Track)
admin.site.register(Profile_Course)
admin.site.register(Track_Course)
admin.site.register(Prerequisite)



