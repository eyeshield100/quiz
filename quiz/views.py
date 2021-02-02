from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Choice
# Create your views here.
class QuestionListView(ListView):
 model=Question
 template_name= "home.html"

def detail(request, pk):
  try:
    question = Question.objects.get(pk=pk)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'question_detail.html', { 'question': question })

def check(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'question_detail.html', {
            'question': question,
        })
    else:
        correct= False
        if selected_choice.choice_text == question.answer:
          correct=True
        context = {'question': question,'correct': correct}
        return render(request, 'results.html', context)