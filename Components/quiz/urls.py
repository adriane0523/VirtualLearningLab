from django.urls import path, re_path
from . import views

urlpatterns = [

    path('<course_id>/', views.QuizListView, name='quiz_index'),

    path('<course_id>/gradebook/', views.viewQuizScoresByCourse, name='course_progress'),

    re_path(r'^category/$',
        views.CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    re_path(r'^category/(?P<category_name>[\w|\W-]+)/$',
        views.ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    re_path(r'^progress/$',
        views.QuizUserProgressView.as_view(),
        name='quiz_progress'),

    re_path(r'^marking/$',
        views.QuizMarkingList.as_view(),
        name='quiz_marking'),

    re_path(r'^marking/(?P<pk>[\d.]+)/$',
        views.QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    re_path(r'^(?P<slug>[\w-]+)/$',
        views.QuizDetailView.as_view(),
        name='quiz_start_page'),

    re_path(r'^(?P<quiz_name>[\w-]+)/take/$',
        views.QuizTake.as_view(),
        name='quiz_question'),
]
