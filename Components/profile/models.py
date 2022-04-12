from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMINISTRATOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMINISTRATOR, 'Administrator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    bio = models.TextField(max_length=250, blank=True, default="Hey, this is my bio...")
    first_name = models.CharField(max_length=30, blank=False,default="")
    last_name = models.CharField(max_length=30, blank=False, default="")
    grade_level = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='profiles/')#, default='default_pfp.jpg'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

     # returns the url to 'profile_detail.html' 
    def get_absolute_url(self):
        return reverse("profile_detail")  

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        print('new user and profile added')

    Profile.objects.get_or_create(user=instance)
    if not instance.is_staff:
        instance.profile.role = 1

    instance.profile.save()

