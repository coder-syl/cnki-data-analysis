from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path,re_path
from cnki.consumer import *



# routing.py路由文件跟django的url.py功能类似，语法也一样，意思就是访问websocket接口


websocket_urlpatterns = [
    path(r"ws/chat/", ChatConsumer),

]

# 这里规定了去哪里找websocket的接口
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})