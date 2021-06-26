<template>
  <div class="cnki-header">
    <div class="navbar">
      <!-- 左边图片区 -->
      <div class="navbar-left">
        <router-link to="/" class="navbar-brand">
          <img src="../assets/img/logo.png" alt="logo" />
        </router-link>
      </div>
      <div class="navbar-right">
        <ul>
          <li class="menu">
            <a href="#">菜单</a>
          </li>
          <li
            v-for="(item,index) in linkList"
            :key="index"
            @click="curActive = index"
            :class="curActive === index ? 'link-active':''"
          >
            <router-link :to="item.link">{{item.des}}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cnki-header",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      curActive: -1,
      menu_show: true,
      linkList: [
        {
          link: "/",
          des: "首页"
        },
        {
          link: "hotAnalyse",
          des: "热门分析"
        },
        {
          link: "onlineSpider",
          des: "在线爬虫"
        },
        {
          link: "chartAnalyse",
          des: "数据分析"
        }
        // {
        //   link: "paperDetail",
        //   des: "论文详情"
        // }
      ]
    };
  },
  methods: {
    showMenu() {
      console.log(this.menu_show);
      this.menu_show = true;
      console.log(this.menu_show);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
li {
  padding: 0;
  list-style: none;
  display: inline-block;
}
.cnki-header {
  width: 80%;
  margin: auto;
  padding: 20px 0 50px 0;
}
.cnki-header .navbar {
  height: 80px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.cnki-header .navbar-brand img {
  width: 125px;
  height: 80px;
}
/* 链接样式 */
.navbar-right {
  display: flex;
  align-items: center;
  justify-content: center;
  /* flex-wrap: wrap; */
  /* padding-left: 50%; */
}

.cnki-header .navbar-right li:first-child {
  display: none;
}
/* .cnki-header .navbar-right li:last-child {
  margin-right: 100px;
} */
.cnki-header .navbar-right li {
  display: inline;
  padding: 20px;
}
.cnki-header .navbar-right li a:hover {
  color: #00aeef;
}
.cnki-header .navbar-right li a {
  color: #000;
  font-size: 1em;
  text-transform: uppercase;
  font-size: 17px;
  font-weight: 300;
}

/* 这里使用交集选择器 */
.link-active >a {
  color: #00aeef !important;
}

@media screen and (max-width: 768px) {
  .menu {
    background: url(../assets/img/menu.png) no-repeat 10px 7px;
  }
  .cnki-header .navbar-right {
  }

  .cnki-header .navbar-right ul {
    width: 120px;
    padding: 0 0;
    position: fixed;
    top: 0;
    right: 15px;
    border: solid 1px #aaa;
    border-radius: 5px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    background-color: #fff;
    opacity: 0.9;
  }
  .cnki-header .navbar-right li {
    display: none;
    padding: 0;
  }
  .cnki-header .navbar-right li:first-child {
    padding-top: 5px;
    display: block;
  }
  .cnki-header .navbar-right a {
    width: 80px;
    display: block;
    padding-left: 32px;
    padding-bottom: 5px;
    text-align: left;
    line-height: 100%;
  }
  .cnki-header .navbar-right ul:hover {
    background: none;
  }
  .cnki-header .navbar-right ul:hover li {
    display: block;
    margin: 0 0 5px;
    width: 80px;
  }
  .cnki-header .navbar {
    height: 80px;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
  .link-active {
  color: #00aeef !important;
  }
}
</style>
