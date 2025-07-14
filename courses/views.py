from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Post
from .forms import RegistrationForm


def index(request):
    courses = Course.objects.all()
    posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'courses/index.html', {'courses': courses, 'posts': posts})


def register(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.course = course
            registration.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'courses/register.html', {'form': form, 'course': course})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def register_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.course = course
            registration.save()
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'course': course})
