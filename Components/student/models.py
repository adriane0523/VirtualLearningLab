from django.db import models
from embed_video.fields import EmbedVideoField
from Components.courses.models import Courses
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    def __str__(self):
        return 'Post: ' + self.title 

    video = EmbedVideoField(blank=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True)
    courses = models.ForeignKey('courses.Courses', related_name="posts",  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    description = models.TextField( default= "", blank=True)

    class Meta:
        # Add verbose name 
        verbose_name = 'Lecture'


class WelcomePage(models.Model):
    def __str__(self):
        return 'Welcome Page: ' + self.title

    title = models.CharField(max_length=255, default ="")
    content = RichTextUploadingField(blank=True)
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    class Meta: 
        # Add verbose name 
        verbose_name = 'Welcome Pages/Home Page'

class ReadingMaterial(models.Model):
    def __str__(self):
        return 'Reading Material: ' + self.title

    title = models.CharField(max_length=255, default ="")
    description = models.TextField(blank=True)
    content = RichTextUploadingField(blank=True)
    link = models.CharField(max_length=2500, default ="", blank=True)
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    class Meta: 
      
        # Add verbose name 
        verbose_name = 'Reading Material'

class Connect(models.Model):
    def __str__(self):
        return 'Connect: ' + self.title
    title = models.CharField(max_length=255, default ="")
    content = RichTextUploadingField(blank=True)
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )

    class Meta: 
        # Add verbose name 
        verbose_name = 'Connect Page'