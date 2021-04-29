from django.urls import path
from Components.courses import views

urlpatterns = [
    path('', views.course, name='course'),
]