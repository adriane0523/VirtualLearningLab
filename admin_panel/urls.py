from django.urls import path
from admin_panel import views

urlpatterns = [
    path('', views.admin, name='admin'),
]