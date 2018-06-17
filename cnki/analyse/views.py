from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

from spider.paper_spider import paperSpider

def index(request):
    # return HttpResponse('nihao');
    return render(request,'analyse/index.html')
def spider(request):
    a=4
    res=paperSpider.delay()
    print(a)
    # print("async task res", res.get())

    # return HttpResponse('res %s' % res.get())
    return render(request,'analyse/spiderStatus.html');
