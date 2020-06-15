from django.db import models

class Zoom(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length = 255) 
    body = models.TextField()
    date = models.CharField(max_length=255)
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )