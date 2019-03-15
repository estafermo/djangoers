from django.shortcuts import render, HttpResponse
from .models import BlogPost
from django.template import loader
from elasticsearch_dsl import DocType, Text, Date, Search
# Create your views here.

def index(request):

    if request.method == 'GET':
        latest_question_list = BlogPost.objects.all
        template = loader.get_template('blog/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        a = request.POST.get("searchtext", "")
        print("AAAAA => ", a)
        s = Search().filter('term', text=request.POST.get("searchtext", ""))
        b = s.execute()
        print("AAAAA => ", b)
        template = loader.get_template('blog/index.html')
        context = {
            'latest_question_list': s.execute(),
        }
        return HttpResponse(template.render(context, request))
    #return HttpResponse(latest_question_list)
    # return HttpResponse("Hello, world. You're at the polls index.")