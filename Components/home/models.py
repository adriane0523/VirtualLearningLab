from django.db import models

# Create your models here.
class HomeNotification(models.Model):
    message = models.TextField(max_length = 200)
    active = models.BooleanField(default=True)

    class Meta: 
        # Add verbose name 
        verbose_name = 'Home Page Notification'