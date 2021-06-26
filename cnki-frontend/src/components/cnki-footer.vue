<template>
  <div class="footer">
    <div class="footer-container">
      <!-- < class="footer-content"> -->
      <img src="../assets/img/under.png" alt />
      <div class="footer-content-online">
        <form>
          <div class="form-group">
            <h2>在线联系</h2>
          </div>
          <div class="form-group">
            <input type="text" name="name" required="required" placeholder="您的姓名" />
          </div>
          <div class="form-group">
            <input type="email" name="email" required="required" placeholder="您的邮箱" />
          </div>
          <div class="form-group">
            <textarea name="message" id="message" required rows="8" placeholder="您的建议或者疑惑"></textarea>
          </div>
          <div class="form-group">
            <button name="submit" class="btn-submit" value="Submit" id="submit">提交</button>
          </div>
        </form>
      </div>
      <div class="footer-content-phone">
        <h2>联系方式</h2>
        <p>QQ: 2522011411</p>
        <p>Phone: 18796323596</p>
        <p>
          Email
          <a href="mailto:someone@example.com">2522011411@qq.com</a>
        </p>
        <h2 class="address">地址</h2>
        <p>江苏省徐州市</p>
        <p>泉山区江苏师范大学</p>
      </div>

      <!-- </div> -->
    </div>
    <div class="footer-content">
      <div class="footer-content-copyright">
        <p>&copy; 知网大数据 2019. All Rights Reserved.</p>
        <p>
          Designed by
          <a target="_blank" href="http://sylblog.xin">尚衍亮</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cnki-footer",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  background: url(../assets/img/footer.png) 0 100% repeat-x;
}
.footer-container {
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
}
.footer-content-phone {
  flex: 1;
  align-items: center;
  max-width: 50%;
  min-width: 50%;
}
.footer-content-online {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  max-width: 50%;
  min-width: 50%;
}
img {
  width: 100%;
}
form {
  width: 70%;
  margin: auto;
}
.form-group {
  padding-top: 5px;
}
.footer-content-online input,
textarea {
  background-color: #fff;
    background-image: none;
    border-radius: 4px;
    border: 1px solid #dcdfe6;
    box-sizing: border-box;
    color: #606266;
    display: inline-block;
    font-size: inherit;
    height: 40px;
    line-height: 40px;
    outline: none;
    padding: 0 15px;
    transition: border-color .2s cubic-bezier(.645,.045,.355,1);
    width: 100%;
    cursor: pointer;;
}
.footer-content-online input:focus,
textarea:focus ,.btn-submit:hover{
border-color: #409eff
}
.footer-content-online textarea {
  height: 100px;
}
.btn-submit {
  width: 100%;
  background-color: transparent;
  padding: 12px 25px;
  font-size: 18px;
  font-weight: 300;
  border: 1px solid #dcdfe6;
  border-radius: 5px;
}

h2 {
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 24px;
  color: #686868;
  font-weight: 300;
  text-align: center;
}
.footer-content-phone p {
  text-align: center;
  padding-top: 10px;
  font-weight: 300;
  font-size: 18px;
  line-height: 22px;
  color: rgb(43, 43, 43);
}
.footer-content-phone p a {
  text-decoration: none;
  color: #c03035;
  font-style: normal;
}
.footer-content-phone .address {
  padding-top: 20px;
}
.footer-content-copyright {
  text-align: center;
  margin-top: 70px;
  /* color: #fff; */
  font-size: 16px;
  padding-bottom: 15px;
}
.footer-content-copyright a {
  color: #3e848a;
}

@media screen and (max-width: 768px) {
  .footer-content-phone,
  .footer-content-online {
    padding-top: 20px;
    max-width: 100%;
    min-width: 100%;
  }
  .footer {
    background: none;
  }
}
</style>
