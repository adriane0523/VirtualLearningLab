from django.shortcuts import render
from Components.courses.models import Courses
from django.contrib.auth.decorators import login_required
from Components.courses.models import Courses
from Components.student.models import Post
@login_required
def course(request):
    courses = Courses.objects.all()
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

    course_progress = zip(enrolled_courses, progress_list)

    # Get all courses
    courses_list = Courses.objects.all()
    context = {
        "courses": courses,
        'enrolled_courses': enrolled_courses,
        'courses_list': courses_list,
        'course_progress': course_progress,
    }
    
    return render(request, "course.html", context)
