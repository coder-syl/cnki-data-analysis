from channels.generic.websocket import WebsocketConsumer
import json
from spider.paper_spider_by_app import start_spider_by_app

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # 连接时触发
        print("开始连接")
        self.accept()
        print('self.channel_name',self.channel_name)

        # self.send(text_data=json.dumps({"message": "message"}))
    def disconnect(self, code):
        # 关闭连接时触发
        # print('关闭连接')
        #
        # try:
        #     self.browser.quit();
        # except Exception as e:
        #     print("关闭出错啦=====================\n", e)
        #     self.browser.quit()
        # 关闭当前执行的爬虫任务
        self.result.revoke(terminate=True)
        # 关闭当前的socket通信
        self.close()
        print('关闭连接')

    def receive(self, text_data=None, bytes_data=None):
        print("收到消息")
        print("==========",text_data)
        print(json.loads(text_data)['keyWords'])
        print('self.channel_name',self.channel_name)
        self.keyWords=json.loads(text_data)['keyWords']
        self.user=json.loads(text_data)['user']
        try:
            self.result = start_spider_by_app.delay(self.keyWords, self.user, self.channel_name)
        except Exception:
            print("出错啦",Exception)
    # start_spider_by_app.delay(self)

    def send_message(self, event):
        print(event)
        print('self.result',self.result)
        self.send(json.dumps({
            "paperInfo": event["message"]
        }))