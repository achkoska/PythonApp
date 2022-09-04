from django.contrib import admin
from .models import Course, Profile, Quiz

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Course,CourseAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile,ProfileAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Quiz,QuizAdmin)