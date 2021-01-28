from django.urls import path
from Components.home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.register, name = 'register'),
  

]