<template>
  <div class="slider">
    <div class="slider-container">
      <div class="slider-left animated fadeInLeftBig">
        <div class="slider-left-title">
          <h1>知网大数据</h1>
        </div>
        <div class="slider-left-dec">
          <p>本系统采用Django+Celery实现在线知网爬虫，并针对爬取的数据进行实时的数据分析</p>
        </div>
        <div class="slider-left-welcome">
          <button>欢迎使用</button>
        </div>
      </div>
      <div class="slider-right animated bounceInDown">
        <img class src="../../assets/img/analyse.png" alt />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "index-slider"
};
</script>>
<style lang="css" scoped>
/* @import url(../../assets/css/animate.css); */
.slider {
  background: url(../../assets/img/sliderBg.png) 0 100% repeat-x;
}
.slider-container {
  /* background:  url("../assets/img/sliderBg.png") ; */
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  /* height: 450px; */
}
.slider-left {
  /* width: 40%; */
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.slider-left-title h1 {
  font-size: 36px;
  font-weight: 300;
}
.slider-left-dec p {
  font-size: 16px;
  font-weight: 300;
}
.slider-left-welcome button {
  background-color: transparent;
  padding: 12px 25px;
  font-size: 18px;
  font-weight: 300;
  border: 1px solid #0099ae;
  border-radius: 5px;
}
.slider-right {
  flex: 1;
  display: flex;
  flex-direction: column-reverse;
  /* justify-container: center; */
  /* width: 60%; */
}
.slider-right img {
  margin: 0px;
  /* animation: bounceDown ease-in-out 200ms both；; */
}
@keyframes bounceDown {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-2000px);
    -ms-transform: translateY(-2000px);
    transform: translateY(-2000px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateY(30px);
    -ms-transform: translateY(30px);
    transform: translateY(30px);
  }
  80% {
    -webkit-transform: translateY(-10px);
    -ms-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    -ms-transform: translateY(0);
    transform: translateY(0);
  }
}
</style>
