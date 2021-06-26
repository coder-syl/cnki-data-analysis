<template>
  <div class="keyword-analyse">
    <div class="keyword-analyse-top">
      <div class="item">
        <p class="title">论文发表期刊分布情况</p>
        <rankByJournal :keywordAndUser="keywordAndUser"></rankByJournal>
      </div>
      <div class="item">
        <p class="title">p卡片名称</p>
        <div></div>
        <rankByJournal></rankByJournal>
      </div>
      <div class="item">
        <rankByJournal></rankByJournal>
      </div>
    </div>
    <div class="keyword-analyse-bottom">
      <div class="item">
        <rankByJournal></rankByJournal>
      </div>
      <div class="item">
        <rankByJournal></rankByJournal>
      </div>
      <div class="item">
        <rankByJournal></rankByJournal>
      </div>
    </div>
  </div>
</template>

<script>
import rankByJournal from "@/components/keywordAnalyse/rankByJournal";
export default {
  components: {
    rankByJournal,
  },
  data(){
      return {
          keywordAndUser:{
              username:localStorage.getItem('name'),
              sch_key:"大数据"
          }
      }
  },
  mounted() {
    console.log(this.$route.query.keyWords);
  },
};
</script>

<style lang='scss' scoped>
.keyword-analyse {
  display: flex;
  flex-direction: column;
}
.keyword-analyse-top,
.keyword-analyse-bottom {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  .item {
    flex: 1;
    border: 1px solid #ededf3;
    margin: 5px;
    position: relative;
    .title {
        padding:10px;
        background: #f6f2f2;
        color:rgb(26, 149, 187);
    //   position: absolute;
    //   top: 0x;
 
    }
  }
}
</style>