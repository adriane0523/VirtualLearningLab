from django.db import models
import uuid 

class Courses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = True) 

    def __str__(self):
        return 'Course: ' + self.name
