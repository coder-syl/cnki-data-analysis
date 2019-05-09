from django.shortcuts import render

import redis
import json
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from spider.paper_spider import paperSpider

import smtplib
from email.mime.text import MIMEText

from .models import Paper
from .models import Keyword
from .models import Year
from .models import YearToKeyword
from .models import Author
from .models import AuthorToKeyword
from .models import Fund
from .models import FundToKeyword
from .models import School
from .models import SchoolToKeyword
from .models import PaperToAuthor

user = {
    'name': '尚衍亮',
}


def index(request):
    return render(request, 'analyse/index.html', user)


def paperDetail(request):
    data = []
    title = ''
    if 'title' in request.GET:
        title = request.GET['title']
        print(title);
    paper=Paper.objects.get(title=title)
    paper_id = paper.id
    print(paper_id)
    author_ids = PaperToAuthor.objects.filter(paper_id_id=paper_id).values('author_id_id')
    for author_id in author_ids:
        author = Author.objects.get(id=author_id['author_id_id']).author
        if author not in data:
            print(author_id['author_id_id'], author)
            data.append(author)
    return render(request, 'analyse/paperDetail.html', {'title': title, 'data': data,'paper':paper})


def paperAnalyse(request):
    keywords = Keyword.objects.all().order_by('-counts');
    return render(request, 'analyse/paperAnalyse.html', {'keywords': keywords})


def startSpider(request):
    return render(request, 'analyse/startSpider.html', user)


def message(request):
    name = request.GET['name'];
    email = request.GET['email']
    message = request.GET['message']

    print(name,email,message)
    msg_from = '2522011411@qq.com'  # 发送方邮箱
    passwd = 'gllmvbsubpovebgd'  # 填入发送方邮箱的授权码
    msg_to = '1094754411@qq.com'  # 收件人邮箱

    subject = "用户发送的邮件"  # 主题
    content = '用户:    '+name+"\n"+"邮箱:      "+email+"\n"+message  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        result = {"status": "ok", "msg": None}

    except Exception as e:
        result = {"status": "ng", "msg": None}
    return HttpResponse(json.dumps(result));


def spider(request):
    request.encoding = 'utf-8'
    if 'keyWord' in request.GET:
        keyWord = request.GET['keyWord']
        context = {
            'keyWord': keyWord,
            'name': '尚衍亮',
        }

    else:
        message = '你提交了空表单'
        # print(message)
        return HttpResponse(message)
    print('提交了关键词', keyWord)
    paperSpider.delay(keyWord)

    return render(request, 'analyse/spiderStatus.html', context)


def getSpiderData(request):
    keyWord = request.GET['keyWord']
    request.session['keyword'] = keyWord
    data = {}
    paper = Paper.objects.filter(sch_key=keyWord).values("id", "title", 'public_year', 'local_url')
    data['data'] = list(paper)
    return HttpResponse(json.dumps(data))


def chart(request):
    keyword = request.session.get('keyword', default=None)
    # keyword = '大数据'
    print(keyword)
    return render(request, 'analyse/chart.html', user)


def getYearToKeyword(request):
    keyword = request.session.get('keyword', default=None)
    # keyword = '大数据'
    datas = []
    # 获取到当前关键词的数据
    keyWord_id = Keyword.objects.get(keyword=keyword)
    print(keyWord_id.id)
    years = YearToKeyword.objects.filter(keyword_id_id=keyWord_id.id).order_by('-year_id_id')

    for year in years:
        data = []
        print(year.year_id_id)
        year_year = Year.objects.filter(id=year.year_id_id)[0]
        print(year_year)
        count = YearToKeyword.objects.filter(keyword_id_id=keyWord_id.id, year_id_id=year.year_id_id)[0]
        print(year_year.year, count.counts)
        data.append(year_year.year)
        data.append(count.counts)
        datas.append(data)
        # data.append(count.count)
    dataset = []
    for data in datas:
        if data not in dataset:
            dataset.append(data)
    print(dataset)
    return HttpResponse(json.dumps(dataset))


def getAuthorToKeyword(request):
    keyword = request.session.get('keyword', default=None)
    # keyword = '大数据'
    datas = []
    # 获取到当前关键词的ID
    keyWord_id = Keyword.objects.get(keyword=keyword)
    print(keyWord_id.id)
    authors = AuthorToKeyword.objects.filter(keyword_id_id=keyWord_id.id)
    for author in authors:
        data = []
        author_name = Author.objects.filter(id=author.author_id_id)[0]
        count = AuthorToKeyword.objects.filter(keyword_id_id=keyWord_id.id, author_id_id=author.author_id_id)[0]
        print(author_name.author, count.counts)
        data.append(author_name.author)
        data.append(count.counts)
        datas.append(data)
    dataset = []
    for data in datas:
        if data not in dataset:
            dataset.append(data)
    return HttpResponse(json.dumps(dataset))


def getFundToKeyword(request):
    keyword = request.session.get('keyword', default=None)
    # keyword = '大数据'
    datas = []
    # 获取到当前关键词的数据
    keyWord_id = Keyword.objects.get(keyword=keyword)
    print(keyWord_id.id)
    funds = FundToKeyword.objects.filter(keyword_id_id=keyWord_id.id).order_by('-fund_id_id')

    for fund in funds:
        data = []
        print(fund.fund_id_id)
        fund_fund = Fund.objects.filter(id=fund.fund_id_id)[0]
        print(fund_fund)
        count = FundToKeyword.objects.filter(keyword_id_id=keyWord_id.id, fund_id_id=fund.fund_id_id)[0]
        print(fund_fund.fund, count.counts)
        data.append(fund_fund.fund)
        data.append(count.counts)
        datas.append(data)
        # data.append(count.count)
    dataset = []
    for data in datas:
        if data not in dataset:
            dataset.append(data)
    print(dataset)
    return HttpResponse(json.dumps(dataset))


def getSchoolToKeyword(request):
    keyword = request.session.get('keyword', default=None)
    # keyword = '大数据'
    datas = []
    # 获取到当前关键词的数据
    keyWord_id = Keyword.objects.get(keyword=keyword)
    print(keyWord_id.id)
    schools = SchoolToKeyword.objects.filter(keyword_id_id=keyWord_id.id).order_by('-school_id_id')

    for school in schools:
        data = []
        print(school.school_id_id)
        school_school = School.objects.filter(id=school.school_id_id)[0]
        print(school_school)
        count = SchoolToKeyword.objects.filter(keyword_id_id=keyWord_id.id, school_id_id=school.school_id_id)[0]
        print(school_school.school, count.counts)
        data.append(school_school.school)
        data.append(count.counts)
        datas.append(data)
        # data.append(count.count)
    dataset = []
    for data in datas:
        if data not in dataset:
            dataset.append(data)
    print(dataset)
    return HttpResponse(json.dumps(dataset))
