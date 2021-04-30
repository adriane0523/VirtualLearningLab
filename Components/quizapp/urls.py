
from django.urls import path
from Components.quizapp import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.examonline, name='quiz')
]
