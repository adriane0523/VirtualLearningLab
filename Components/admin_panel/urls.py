from django.urls import path
from Components.admin_panel import views

urlpatterns = [
    path('', views.admin, name='admin'),
]