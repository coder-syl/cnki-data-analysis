<template>
  <div class="index">
    <indexSlider></indexSlider>
    <indexService></indexService>
    <indexData></indexData>
    <indexFeature></indexFeature>
  </div>
</template>

<script>
import indexSlider from "../components/index/index-slider.vue";
import indexService from "../components/index/index-service.vue";
import indexData from "../components/index/index-data.vue";
import indexFeature from "../components/index/index-feature.vue";
export default {
  components: {
    indexSlider,
    indexService,
    indexData,
    indexFeature
  },

  data() {
    return {
      msg: "这是首页"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
