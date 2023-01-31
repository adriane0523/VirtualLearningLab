from django.db import models
import uuid

class Courses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = True) 
    users = models.ManyToManyField('auth.User', verbose_name='Students',
                                    related_name='courses', default=None, blank=True)


    def __str__(self):
        return 'Course: ' + self.name
        
    class Meta: 
        # Add verbose name 
        verbose_name = 'Courses/Classe'

    # returns the url to the particual discussions 'discussion_detail.html' 
    def get_absolute_url(self):
        return reverse("class_detail", kwargs={'id_field': self.courses.id}) #

    def courseNum(self):
        return len(self.users.count())
