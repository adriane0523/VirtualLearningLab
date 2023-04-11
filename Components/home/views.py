from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import HomeNotification
from Components.courses.models import Courses

from Components.student.models import Post



def home(request):
    
    if(request.user.is_authenticated):
        # Get the enrolled courses list
        enrolled_courses = request.user.courses.all()

        progress_list = []

        for course in enrolled_courses:
            posts = Post.objects.all().filter(courses = (str)(course.id) )
            num = 0
            for post in posts:
                if post.completed == True:
                    num += 1
            progress_list.append(int((num/len(posts)) * 100))
        

        # Get all courses
        courses_list = Courses.objects.all()

        course_progress = zip(enrolled_courses, progress_list)
    
    # Get all active HomeNotifications and send them to the homepage template
    notifications = HomeNotification.objects.all().filter(active=True)

    # percent = request.session['percent']
    
    if(request.user.is_authenticated):
        context = {
            'notifications': notifications,
            'enrolled_courses': enrolled_courses,
            'courses_list': courses_list,
            'course_progress': course_progress,
            }
    else:
        context = {
            'notifications': notifications,
        }

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/accounts/login/?next=/')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'sign_up.html', {'form': f})

def about_view(request):

    if(request.user.is_authenticated):
        enrolled_courses = request.user.courses.all()
        progress_list = []

        for course in enrolled_courses:
            posts = Post.objects.all().filter(courses = (str)(course.id) )
            num = 0
            for post in posts:
                if post.completed == True:
                    num += 1
            progress_list.append(int((num/len(posts)) * 100))
        
        courses_list = Courses.objects.all()

        course_progress = zip(enrolled_courses, progress_list)

        context = {
                'enrolled_courses': enrolled_courses,
                'courses_list': courses_list,
                'course_progress': course_progress,
                }
    else:
        context = {}
    return render(request, 'about.html', context)

def teams_view(request):

    if(request.user.is_authenticated):
        enrolled_courses = request.user.courses.all()
        progress_list = []

        for course in enrolled_courses:
            posts = Post.objects.all().filter(courses = (str)(course.id) )
            num = 0
            for post in posts:
                if post.completed == True:
                    num += 1
            progress_list.append(int((num/len(posts)) * 100))
        
        courses_list = Courses.objects.all()

        course_progress = zip(enrolled_courses, progress_list)

        context = {
                'enrolled_courses': enrolled_courses,
                'courses_list': courses_list,
                'course_progress': course_progress,
                }
    else:
        context = {}
    return render(request, 'teams.html', context)