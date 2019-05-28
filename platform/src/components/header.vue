<template>
  <div class="header-inner">
    <div class="logo">
      <!-- <router-link :to="{path: '/'}">
        <img src="../assets/logo.png">
      </router-link> -->
    </div>
    <div class="header-nav">
      <ul>
        <li><router-link to="/">首页</router-link></li>
        <li>页面1</li>
        <li>页面2</li>
        <li>页面3</li>
      </ul>
      <div class="head-login text-center">
        <keep-alive>
          <router-link to="/login" v-if="!mystudy">登陆/注册</router-link>
          <router-link to="/my"  v-if="mystudy">{{ mystudy }}</router-link>
        </keep-alive>
      </div>
    </div>
    <div class="header-right">
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 接收session中存储的登陆信息
      mystudy: sessionStorage.mystudy
    }
  }
}
</script>

<style lang="less" scoped>
.header-inner{
  width: 100%;
  height: 60px;
  background: transparent;
  position: absolute;
  top: 30px;
  z-index: 100;
  font-size: 16px;
  .logo{
    float: left;
    width: calc(50% - 575px);
    height: inherit;
    img{
      width: 100px;
      height: 50px;
      margin: auto;
    }
  }
  .header-nav{
    width: 1150px;
    height: inherit;
    line-height: 60px;
    float: left;
    text-align: right;
    color: @font-white;
    ul{
      display: inline-block;
      padding-right: 80px;
      li{
        display: inline-block;
        color: #d7d5ff;
        padding-right: 10px;
      }
    }
    .head-login{
      color: #fff;
      display: inline-block;
      background: #5280e7;
      cursor: pointer;
      border-radius: 20px;
      width: 138px;
      height: 34px;
      line-height: 34px;
      padding: 1px 15px;
      box-shadow: 0px 28px 16px -6px rgba(39, 76, 160, .6);
    }
  }
  .header-right{
    float: left;
    width: calc(50% - 575px);
    height: inherit;
    line-height: 60px;
    // ul{
    //   li{
    //     display: inline-block;
    //   }
    // }
  }
}
</style>
