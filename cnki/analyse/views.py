from django.shortcuts import render

import redis
import json
# Create your views here.
from django.template import loader
from django.http import HttpResponse

from spider.paper_spider import paperSpider


def index(request):
    return render(request, 'analyse/index.html')


def paperAnalyse(request):
    return render(request, 'analyse/paperAnalyse.html')


def startSpider(request):
    return render(request, 'analyse/startSpider.html')


def spider(request):
    request.encoding = 'utf-8'
    if 'keyWord' in request.GET:
        keyWord = request.GET['keyWord']
        context = {
            'keyWord': keyWord,
        }

    else:
        message = '你提交了空表单'
        # print(message)
        return HttpResponse(message)

    data = paperSpider.delay(keyWord)

    return render(request, 'analyse/spiderStatus.html', context)


def getSpiderData(request):
    keyWord = request.GET['keyWord']
    conn = redis.Redis(host='127.0.0.1', port=6379, db=1)
    spider_datas = conn.smembers(keyWord)
    data = []
    for i in spider_datas:
        spider_data = {}
        spider_data['title'] = i.decode("utf-8")
        print(i.decode("utf-8"))
        data.append(spider_data)

    return HttpResponse(json.dumps(data))
