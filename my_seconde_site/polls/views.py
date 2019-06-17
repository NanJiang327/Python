from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
# Create your views here.
from .models import Choice, Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     '''''
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))
#     '''''
#     return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
    # 默认情况下，通用视图 DetailView 使用一个叫做 <app name>/<model name>_detail.html 的模板。
    # 在我们的例子中，它将使用 "polls/question_detail.html" 模板。
    # template_name 属性是用来告诉 Django 使用一个指定的模板名字，而不是自动生成的默认名字。
    # 我们也为 results 列表视图指定了 template_name —— 这确保 results 视图和 detail 视图在渲染时具有不同的外观，
    # 即使它们在后台都是同一个 DetailView 
    model = Question
    template_name = 'polls/results.html'


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question doesn't exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['selected'])
    # 如果在request.POST['choice']数据中没有提供choice ，
    # POST将引发一个KeyError 。上面的代码检查KeyError ，如果没有给出
    # choice将重新显示Question表单和一个错误信息。
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_text': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))