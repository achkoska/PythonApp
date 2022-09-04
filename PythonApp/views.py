
from django.shortcuts import render, redirect
from .models import Course, Profile,Quiz
from datetime import datetime
from .forms import CourseForm
# Create your views here.


def index(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect("courses")
    queryset = Course.objects.filter(user=request.user).all()
    context = {"courses": queryset, "Date":datetime.now().date(), "form":CourseForm}
    return render(request, "index.html",context= context)
