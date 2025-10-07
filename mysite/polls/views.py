from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
#from django.template import loader
from django.http import Http404
from django.shortcuts import render,get_object_or_404


def index(request):
    latest_question_list=Question.objects.orderby("pub_date")[:5]
    #template=loader.get_template("polls/index.html")
    #output=", ".join([q.question_text for q in latest_question_list])
    context={'latest_question_list':latest_question_list}
    #return HttpResponse(template.render(context,request))
    return  render(request,"polls/index.html",context)

# Create your views here.
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    #try:
        #question=Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question doesnt exis")
    #return HttpResponse("You are looking at question %s."% question_id)
    return render(request,"polls/detail.html",{"question":question})



def results(request,question_id):
    response="You are looking at the results of question %s." 
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s."% question_id)



