from django.urls import path
from . import views

urlpatterns = [

    path( "<id_field>", views.class_zoom, name="class_zoom"),
]