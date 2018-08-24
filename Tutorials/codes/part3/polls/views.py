from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader #导入模板加载器
from .models import Question
from django.shortcuts import render,get_object_or_404
# Create your views here.

#def index(request):
#    return HttpResponse("hello world. You're at the polls index.")

#def index(request):
#    """
#    """
#    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#    output = ','.join([question.question_text for question in latest_question_list])
#    return HttpResponse(output)

#def index(request):
#    """
#    """
#    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] #查询数据
#    template = loader.get_template('polls/index.html')                      #加载模板
#    context={'latest_question_list':latest_question_list}                   #构造上下文
#    return HttpResponse(template.render(context,request))                   #返回渲染后的页面

def index(request):
    """
    """
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] #查询数据
    context={'latest_question_list':latest_question_list}                   #构造上下文
    return render(request,'polls/index.html',context=context)               #渲染页面并返回


#def detail(request,question_id):
#    """
#    """
#    return HttpResponse("you are looking at question {0}".format(question_id))

#def detail(request,question_id):
#    """
#    """
#    try:
#        question = Question.objects.get(pk=question_id) #从数据库中查询对象
#    except Question.DoesNotExist as e:                  #如果没有找到对应的对象，那么就直接报404异常
#        raise Http404("question {0} does not exist".format(question_id)) #注意404不是一个HttpResponse面是一个Exception
#    context={'question':question}                       #如果能直接到这里说明有这个对象存在，那么构造上下文
#    return render(request,'polls/detail.html',context=context)

def detail(request,question_id):
    """
    """
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    """
    """
    return HttpResponse("your are looking at result of question {0}".format(question_id))

def vote(request,question_id):
    """
    """
    return HttpResponse("you are voting on question {0}".format(question_id))
