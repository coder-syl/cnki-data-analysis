from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from analyse import views

urlpatterns = [
                  # 首页
                  path('', views.index, name="index"),
                  # 登录
                  path('login', views.doLogin, name="login"),
                  # 注册
                  path('register', views.doRegister, name="register"),
                  # 登出
                  path('logout', views.doLogout, name="logout"),
                  # 分析
                  path('paperAnalyse', views.paperAnalyse, name="paperAnalyse"),
                  # 开启爬虫
                  path('startSpider', views.startSpider, name="startSpider"),
                  # 爬虫
                  path('spider', views.spider, name="spider"),
                  path('message', views.message, name="message"),
                  # 从redis中获取到爬取状态
                  path('get_spider_data', views.getSpiderData, name="getSpiderData"),
                  path('chart', views.chart, name="chart"),
                  path('getYearToKeyword', views.getYearToKeyword, name="getYearToKeyword"),
                  path('getAuthorToKeyword', views.getAuthorToKeyword, name="getAuthorToKeyword"),
                  path('getFundToKeyword', views.getFundToKeyword, name="getFundToKeyword"),
                  path('getSchoolToKeyword', views.getSchoolToKeyword, name="getSchoolToKeyword"),
                  path('paperDetail', views.paperDetail, name="paperDetail"),
                  path('rankByJournal', views.rankByJournal, name="rankByJournal")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
