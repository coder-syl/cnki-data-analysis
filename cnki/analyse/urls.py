from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from analyse import views

urlpatterns = [
                  path('', views.index, name="index"),
                  path('startSpider', views.startSpider, name="startSpider"),
                  path('spider', views.spider, name="spider"),
                  path('get_pider_data', views.getSpiderData, name="getSpiderData")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
