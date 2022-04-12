from django.urls import path
from Components.home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.register, name = 'register'),
    path('about/', views.about_view, name = 'about'),
    path('teams/', views.teams_view, name = 'teams'),
    

]