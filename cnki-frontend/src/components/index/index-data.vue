<template>
  <div class="data">
    <div class="data-container">
      <div class="data-content" v-for="item in content" :key="item.title">
        <div class="data-content-title">
          <h1 data-to="7000" data-speed="3000" data-from="0">{{item.title}}</h1>
        </div>
        <div class="data-content-dec">
          <h3>{{ item.dec}}</h3>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "index-data",
  data() {
    return {
      content: [
        {
          title: "7000",
          dec: "论文"
        },
        {
          title: "100",
          dec: "发表者"
        },
        {
          title: "432",
          dec: "关键词"
        },
        {
          title: "145",
          dec: "高校"
        }
      ]
    };
  }
};
</script>>
<style lang="css" scoped>
.data {
  background-color: #fbfafa;
}
.data-container {
  /* background:  url("../assets/img/sliderBg.png") ; */
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  /* height: 450px; */
}
.data-content {
  /* width: 30%; */
  display: flex;
  flex: auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.data-content-title {
  padding-top: 15px;
  padding-bottom: 30px;
}
.data-content-title h1 {
  font-weight: 200;
  font-size: 40px;
  color: #00aeef;
  height: 30px;
}
.data-content-dec {
  padding-bottom: 15px;
}
.data-content-dec h3 {
  font-size: 18px;
  font-weight: 300;
}
</style>
