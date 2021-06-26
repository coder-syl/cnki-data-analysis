<template>
  <div class="hotAnalyse">
    <div class="hotAnalyse-container">
      <h1>热门查询</h1>
      <div class="hotAnalyse-content">
        <div class="hotAnalyse-content-box" v-for="(item,index) in existData" :key="index">
          <div class="box-rank">{{index+1}}</div>
          <div class="box-content">
            <div>
              <img :src="require('../assets/img/hot/icon-item00'+(index%6+1)+'.png')" alt />
            </div>
            <div class="box-content-num">{{item.num}}</div>
            <div class="box-content-title">{{item.title}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: "hotAnalyse",
  data() {
    return {
      existData: [
        { link: "", title: "大数据", num: 12342 },
        { link: "", title: "农林牧渔", num: 1234 },
        { link: "", title: "卫生", num: 123847 },
        { link: "", title: "科学研究", num: 12348 },
        { link: "", title: "交通运输", num: 123840 },
        { link: "", title: "信息技术", num: 1283233 },
        { link: "", title: "社会服务", num: 12340 },
        { link: "", title: " 公共图书馆", num: 10234 },
        { link: "", title: "旅游", num: 12340 },
        { link: "", title: "建筑材料", num: 12344 },
        { link: "", title: "城乡规划", num: 129342 },
        { link: "", title: "大数据", num: 121340 },
        { link: "", title: "信息通信", num: 10234 },
        { link: "", title: " 金融", num: 12340 },
        { link: "", title: "创业创新", num: 18642340 },
        { link: "", title: "应急管理", num: 1248440 },
        { link: "", title: "科普", num: 10234 },
        { link: "", title: "全民健身", num: 12340 }
      ]
    };
  },
  mounted() {
    this.existData.sort(function(a, b) {
      return b.num - a.num;
    });
  },
  methods: {
    renderImg() {
      return;
    }
  }
};
</script>

<style scoped>
.hotAnalyse-container {
  width: 80%;
  margin: auto;
  padding-bottom: 20px;
}
.hotAnalyse-container h1 {
  text-align: center;
  margin-bottom: 30px;
}

.hotAnalyse-content {
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.hotAnalyse-content-box {
  visibility: visible;
  animation-duration: 0.4s;
  animation-delay: 0s;
  animation-iteration-count: 1;
  border: 1px solid #eee;
  padding: 30px 80px;
}
.box-content {
  flex: auto;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.hotAnalyse-content-box:hover {
  -webkit-box-shadow: rgba(1, 130, 150, 0.2) 0px 0px 30px;
  -moz-box-shadow: rgba(1, 130, 150, 0.2) 0px 0px 30px;
  box-shadow: rgba(1, 130, 150, 0.2) 0px 0px 30px;
}
.box-rank {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  line-height: 30px;
  text-align: center;
  border: 1px solid #fff;
  background-color: rgb(6, 180, 122);
  position: relative;
  top: -25px;
  left: -80px;
  color: #eee;
}
.box-content-title {
  color: rgb(253, 176, 33);
}
.box-content-num {
  padding: 10px;
  color: rgb(253, 176, 33);
}
</style>
