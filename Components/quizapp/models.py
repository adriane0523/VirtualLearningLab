from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.

class Quiz(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Weight=models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    Score=models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = True) 
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    def __str__(self):
        return 'Quiz: ' + self.Name

    class Meta:
        db_table="Quiz"

class Question(models.Model):
    Question=models.CharField(max_length=100)
    Option1=models.CharField(max_length=100)
    Option2=models.CharField(max_length=100)
    Option3=models.CharField(max_length=100)
    Option4=models.CharField(max_length=100)
    CorrectAns=models.CharField(max_length=100)
    Points=models.IntegerField(default=1)
    Quiz= models.ForeignKey(Quiz,on_delete=models.CASCADE)
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = True) 

    def __str__(self):
        return 'Question: ' + self.Question

    class Meta:
        db_table="Question"