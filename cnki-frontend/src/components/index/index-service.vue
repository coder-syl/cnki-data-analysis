<template>
  <div class="service">
    <div class="service-container">
      <div class="service-content" v-for="item in content" :key="item.title">
        <div class="service-content-img animated fadeIn"  style="animation-delay: 1s;animation-uration:1s;">
          <img :src="item.imgSrc" alt />
        </div>
        <div class="service-content-title">
          <h2>{{item.title}}</h2>
        </div>
        <div class="service-content-dec">
          <p>{{ item.dec}}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "index-service",
  data() {
    return {
      content: [
        {
          imgSrc: require("@/assets/img/icon1.png"),
          title: "在线智能爬虫",
          dec: "提供关键词，实时开启知网爬虫模块，自动化采集，摒弃人工采集"
        },
        {
          imgSrc: require("@/assets/img/icon2.png"),
          title: "实时数据分析",
          dec:
            "依靠抓取的论文数据，实时分析论文的数据，图表清晰可见，提供分析数据的下载"
        },
        {
          imgSrc: require("@/assets/img/icon3.png"),
          title: "数据下载",
          dec: "数据分析的结果均支持免费下载，当然也支持原始数据下载。"
        }
      ]
    };
  }
};
</script>>
<style lang="css" scoped>
.service-container {
  /* background:  url("../assets/img/sliderBg.png") ; */
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  font-weight:300;
  padding: 50px 0;

  /* height: 450px; */
}
.service-content {
  /* width: 30%; */
  display: flex;
  flex: auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.service-content-dec p{
  width: 60%;
  margin: auto;
  font-weight: 300;
  text-align: center;
}
.service-content-title h2{
  font-weight: 300;
}
</style>
