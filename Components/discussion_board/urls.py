from django.urls import path
from . import views

urlpatterns = [
    path('<id_field>/', views.discussions, name='discussions'),
    path('<id_field>/<int:pk>/', views.discussion_detail, name='discussion_detail'),
    path('<int:pk>/update_comment', views.update_comment, name='update_comment'),
    path('<int:pk>/delete_comment', views.delete_comment, name='delete_comment'),
    path('<int:pk>/upvote_comment', views.upvote_comment, name='upvote_comment'),
    path('<int:pk>/update_reply', views.update_reply, name='update_reply'),
    path('<int:pk>/delete_reply', views.delete_reply, name='delete_reply'),
    path('<int:pk>/upvote_reply', views.upvote_reply, name='upvote_reply'),
]