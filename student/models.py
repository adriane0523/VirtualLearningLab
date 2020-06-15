from django.db import models
from embed_video.fields import EmbedVideoField
from courses.models import Courses
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    def __str__(self):
        return 'Post: ' + self.title 
    video = EmbedVideoField(blank=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
 
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    description = models.TextField( default= "")


class WelcomePage(models.Model):
    def __str__(self):
        return 'Welcome Page: ' + self.title
    title = models.CharField(max_length=255, default ="")
    content = RichTextUploadingField()
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )

class ReadingMaterial(models.Model):
    def __str__(self):
        return 'Reading Material: ' + self.title
    title = models.CharField(max_length=255, default ="")
    description = models.TextField()
    link = models.CharField(max_length=500, default ="")
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )

class Connect(models.Model):
    def __str__(self):
        return 'Connect: ' + self.title
    title = models.CharField(max_length=255, default ="")
    content = RichTextUploadingField()
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
