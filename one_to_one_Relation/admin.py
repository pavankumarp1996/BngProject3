from django.contrib import admin

from django.contrib import admin

from .models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Sno','Sname','Slocation']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['Cid','Cname','Cfee']



admin.site.register(Student,StudentAdmin)

admin.site.register(Course,CourseAdmin)

