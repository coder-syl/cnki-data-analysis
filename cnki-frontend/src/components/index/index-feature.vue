<template>
  <div class="feature">
    <div class="feature-container">
      <div class="feature-left">
        <div class="feature-left-title">
          <h1>知网大数据</h1>
        </div>
        <div class="feature-left-dec">
          <p>通过智能的在线爬虫，实时抓取特定的论文信息，实时针对数据在线分析，快速了解某个领域。同时系统支持在线查找，可查找具体的作者， 学校，论文。实现到点的分析。</p>
        </div>
      </div>
      <div class="feature-right">
        <img class src="../../assets/img/cnki.png" alt />
      </div>
    </div>
    <div class="feature-container">
      <div class="feature-right">
        <img class src="../../assets/img/chart.png" alt />
      </div>
      <div class="feature-left">
        <div class="feature-left-title">
          <h1>可视化图表</h1>
        </div>
        <div class="feature-left-dec">
          <p>精准的可视化数据图表，让数据一览无余，找出数据背后的价值.提供多样式的表格数据展示，满足多种数据阅读需要, 支持灵活地筛选需要观察的数据</p>
        </div>
      </div>
    </div>
    <div class="feature-container">
      <div class="feature-left">
        <div class="feature-left-title">
          <h1>性能稳定的分析平台</h1>
        </div>
        <div class="feature-left-dec">
          <p>将数据分析和爬虫相结合，使用户可以从复杂的代码编写中解放出来，快速的抓取和分析知网数据</p>
        </div>
      </div>
      <div class="feature-right">
        <img class src="../../assets/img/btos.png" alt />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "index-feature"
};
</script>>
<style lang="css" scoped>
.feature {
  padding-bottom: 30px;
}
.feature-container {
  width: 70%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  padding: 30px;
}
.feature-left {
  width: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.feature-left-title h1 {
  text-align: center;
  font-size: 36px;
  font-weight: 300;
}
.feature-left-dec p {
  font-size: 16px;
  font-weight: 300;
  margin: auto;
  text-align: center;
}
.feature-left-welcome button {
  background-color: transparent;
  padding: 12px 25px;
  font-size: 18px;
  font-weight: 300;
  border: 1px solid #0099ae;
  border-radius: 5px;
}
.feature-right {
  width: 50%;
  display: flex;
  justify-content: center;
}
.feature-right img {
  width: 100%;
  height: 100%;
}

@media screen and (max-width: 768px) {
  .feature-right {
    width: 100%;
  }
}
</style>
