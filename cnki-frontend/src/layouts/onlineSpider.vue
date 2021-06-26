<template>
  <div class="onlineSpider">
    <div class="onlineSpider-container">
      <div class="start">
        <input type="text" v-model="keyWord" required="required" />
        <el-button type="primary" @click="startSpider" :disabled="startDisabled"
          >启动爬虫</el-button
        >
        <el-button type="primary" @click="startAnalyse" 
          >分析数据</el-button
        >
        <button @click="closeSpider">关闭爬虫</button>
      </div>
      <div class="steps" v-show="stepsShow">
        <div>
          <button class="steps-button">使用步骤</button>
        </div>
        <div class="steps-content">
          <div class="steps-content-top">
            <div class="steps-content-left">
              <div class="left-content">
                <h2>输入关键词</h2>
                <p>
                  在输入框内输入你要抓取的的相关的关键字，例如大数据，然后回车或者点击开启爬虫按钮。
                </p>
              </div>
            </div>
            <div class="steps-content-right">
              <div class="right-content">
                <h2>等待数据爬取</h2>
                <p>
                  提示爬虫已经启动，然后等待10秒钟，等待系统连接到知网，此时可以实现查看爬取的进度和爬取的相关论文。
                </p>
              </div>
            </div>
          </div>
          <div class="steps-content-top">
            <div class="steps-content-left">
              <div class="left-content">
                <h2>输入关键词</h2>
                <p>
                  在输入框内输入你要抓取的的相关的关键字，例如大数据，然后回车或者点击开启爬虫按钮。
                </p>
              </div>
            </div>
            <div class="steps-content-right">
              <div class="right-content">
                <h2>等待数据爬取</h2>
                <p>
                  提示爬虫已经启动，然后等待10秒钟，等待系统连接到知网，此时可以实现查看爬取的进度和爬取的相关论文。
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="steps" v-show="!stepsShow">
        <el-table :data="tableData" style="width: 100%" max-height="500">
          <el-table-column
            fixed
            prop="title"
            label="文章"
            width="350"
          ></el-table-column>
          <el-table-column
            prop="author"
            label="作者"
            width="120"
          ></el-table-column>
          <el-table-column
            prop="content"
            label="简介"
            width="200"
            show-overflow-tooltip
          ></el-table-column>
          <el-table-column
            prop="source"
            label="来源"
            width="180"
          ></el-table-column>
          <el-table-column
            prop="public_year"
            label="发表时间"
          ></el-table-column>
          <el-table-column
            prop="download"
            label="下载数量"
          ></el-table-column>
          <el-table-column
            prop="cite"
            label="下载数量"
          ></el-table-column>
          <el-table-column label="操作" width="120">
            <template slot-scope="scope">
               <el-link href="scope.link">CNKI<i class="el-icon-view el-icon--right"></i> </el-link>
               <el-link :href="scope.link">分析<i class="el-icon-view el-icon--right"></i> </el-link>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "onlineSpider",
  data() {
    return {
      msg: "在线爬虫",
      keyWord: "",
      stepsShow: true,
      tableData: [],
      chatSocket: undefined,
      startDisabled: false,
    };
  },
  name: "index",
  watch: {
    tableData(val) {
      console.log("变化啦");
      console.log(val);
    },
  },
  created() {
    this.chatSocket = new WebSocket("ws://" + "127.0.0.1:8000" + "/ws/chat/");
    this.chatSocket.onopen=()=>{
      console.log("链接成功")
    }
    window.onbeforeunload = function () {
      // 可以在这里写刷新之前的时间

      return "";
    };
  },
  destroyed() {
    window.onbeforeunload = null;
  },
  methods: {
    closeSpider() {
      console.log("关闭爬虫");
      // this.chatSocket.send("close");
      if (this.chatSocket.readyState === WebSocket.OPEN) {
        this.chatSocket.close();
      }
      // this.chatSocket.close();
    },
    startAnalyse(){
      console.log('分析数据')
      this.$router.push({ name: 'keywordAnalyse', params: { keyWords: 123 }})
    },
    startSpider() {
      this.$message({
        message: "成功连接到数据抓取服务器",
        type: "success",
      });
      this.startDisabled = true;
      this.tableData = [];

      this.stepsShow = false;
      //创建socket连接

      // this.chatSocket.onopen = () =>
      this.chatSocket.send(JSON.stringify({ keyWords: this.keyWord,user:localStorage.getItem('name') }));
      // chatSocket.send();

      // 后端使用send()方法发送的数据，由onmessage接收，并进行处理或展示
      this.chatSocket.onmessage = (e) => {
        console.log("收到消息");
        if (e.data === "202") {
          this.$message({
            message: "开始获取数据",
            type: "success",
          });
        }
        // console.log(e);
        else {
          let data = JSON.parse(e.data);
          this.tableData.unshift(data.paperInfo[0]);
        }
      };
      this.chatSocket.onclose = (e) => {
        this.$message({
          message: "断开与数据抓取服务器的连接" + e,
          type: "error",
        });
        this.startDisabled = false;
      };
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.onlineSpider-container {
  width: 80%;
  margin: auto;
}
.start {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  padding-top: 20px;
}
input {
  width: 50%;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  margin-right: 20px;
  padding: 0 15px;
  font-size: 20px;
  font-weight: 300;
}
input:focus {
  border-color: none;
}
button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  color: #fff;
  background-color: #409eff;
  border: 1px solid #409eff;
  -webkit-appearance: none;
  text-align: center;
  box-sizing: border-box;
  outline: none;
  margin: 0;
  transition: 0.1s;
  font-weight: 500;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  padding: 0.8em 1.5em;
  font-size: 1em;
  border-radius: 4px;
  margin:0px 5px;
}
.steps {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  padding-top: 20px;
}
.steps-button {
  background-color: transparent;
  font-size: 22px;
  color: #00aeef;
  border-color: #88cdf5;
  font-weight: 300;
  border-radius: 0;
  padding: 15px 35px;
}
.steps-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-wrap: wrap;
  padding-top: 20px;
  position: relative;
}
.steps-content::before {
  position: absolute;
  top: 0;
  content: "";
  border: 1px solid #88d8f5;
  left: 50%;
  margin-left: -2px;
  height: 100%;
}
.steps-content-top {
  /* border: 1px solid #000; */
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
}
.steps-content-left {
  /* border-right: 1px solid #000; */
  flex: 1;
  position: relative;
}
.left-content {
  width: 60%;
  margin: auto;
}
.left-content::after {
  position: absolute;
  right: 2px;
  content: "";
  top: 15px;
  background: url(../assets/img/online/left.png);
  width: 43px;
  height: 54px;
}
.steps-content-right {
  flex: 1;
  position: relative;
}
.left-content h2,
.right-content h2 {
  font-weight: 300;
  font-size: 24px;
  color: #0e0d0d;
}

.left-content p,
.right-content p {
  font-weight: 350;
  font-size: 16px;
  line-height: 22px;
  color: #0e0d0d;
}
.right-content {
  width: 60%;
  /* border: 1px solid #000; */
  margin: auto;
  padding-top: 100px;
}
.right-content::before {
  position: absolute;
  left: -2px;
  content: "";
  top: 100px;
  background: url(../assets/img/online/right.png);
  width: 43px;
  height: 54px;
}
</style>
