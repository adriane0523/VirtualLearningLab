from django.urls import path
from . import views

urlpatterns = [
    path("<id_field>/", views.class_index, name="class_index"),
    path("<id_field>/<int:pk>/", views.class_detail, name="class_detail"),
    path("welcome/<id_field>", views.welcome_page, name="welcome_page"),
    path("reading_material/<id_field>", views.reading_material, name="reading_material"),
    path("connect/<id_field>", views.connect, name="connect"),
    # path("quizzes/<id_field>", views.quizzes, name="quiz"),
    # path("quizzes/<id_field>/<int:id>", views.quizzes_index, name="quiz_index"),
]