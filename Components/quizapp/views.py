from django.shortcuts import render
from Components.quizapp.models import Quiz,Question

# Create your views here.
def examonline(request):
    results= Question.objects.all()
    #This should be changed
    #console.log(results)
    context = {
        "Exam":results
    }
    return render(request, 'index.html', context)