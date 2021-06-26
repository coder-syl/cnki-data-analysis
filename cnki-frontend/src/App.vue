<template>
  <div class="app">
    <div class="header">
      <cnkiHeader></cnkiHeader>
    </div>
    <div class="container">
      <router-view />
    </div>
    <div class="footer">
      <cnkiFooter></cnkiFooter>
    </div>
  </div>
</template>
 <script>
import cnkiHeader from "./components/cnki-header";
import cnkiFooter from "./components/cnki-footer";
export default {
  name: "App",
  components: {
    cnkiHeader,
    cnkiFooter
  }
};
</script>
 <style lang="css">
 @import url(./assets/css/animate.css);
 *{
   margin:0;
   padding: 0;
 }
.app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* width: 50%; */
  /* margin-left: 20%; */
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
a {
  text-decoration: none;
}
/* .container {
  height: 600px;
} */
/* 大型设备（大台式电脑，1200px 起） */
/* @media screen and (min-width: 1200px) {

} */
/* 中型设备（台式电脑，992px 起） */
@media screen and (min-width: 992px) {
  .app {
    width: 100%;
    /* margin-left: 20%; */
  }
}
/* 小型设备（平板电脑，768px 起） */
@media screen and (min-width: 768px) and (max-width: 992px) {
  .app {
    /* background-color: lightblue; */
    width: 100%;
    margin-left: 0;
  }
}
/* 超小设备（手机，小于 768px） */
@media screen and (max-width: 992px) {
  .app {
    /* background-color: lightblue; */
    width: 100%;
    margin-left: 0;
  }
}
</style>
