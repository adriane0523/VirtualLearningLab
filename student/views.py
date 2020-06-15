from django.shortcuts import render
from student.models import Post, WelcomePage,ReadingMaterial, Connect

def class_index(request, id_field):
    posts = Post.objects.all().filter(courses = (str)(id_field) )
    print("test")
    context = {
        "posts": posts,
    }
    print(context)
    return render(request, "class_index.html", context)

def class_category(request,id_field, category):
    posts = Post.objects.all().filter(courses = (str)(id_field) )
    detail = posts.get(categories__name__contains=category )


    context = {
        "category": category,
        "posts": detail
    }
    return render(request, "class_category.html", context)

def class_detail(request, id_field, pk):
    posts = Post.objects.all().filter(courses = (str)(id_field) )
    detail = posts.get( pk=pk)
  
    context = {
        "post": detail,
     
    }

    return render(request, "class_detail.html", context)


def welcome_page(request, id_field):
    page = WelcomePage.objects.all().filter(courses = (str)(id_field) )
   
    context = {
        "page": page,
    }

    return render(request, "welcome_page.html", context)

def reading_material(request, id_field):
    page = ReadingMaterial.objects.all().filter(courses = (str)(id_field) )
   
    context = {
        "page": page,
    }

    return render(request, "reading_material.html", context)


def connect(request, id_field):
    page = Connect.objects.all().filter(courses = (str)(id_field) )
   
    context = {
        "page": page,
    }

    return render(request, "connect.html", context)
