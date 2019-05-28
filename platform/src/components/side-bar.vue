<template>
  <div class="sidebar-container">
    <div class="logo">
      <img src="../assets/images/icon/logo.png" />
    </div>
    <div class="avatar center-block">
    </div>
    <!-- 用全局变量default-active绑定当前页面，页面切换时变更该全局变量来实现当前项的变更。 -->
    <el-menu :default-active="$route.path" router >
      <el-menu-item v-for="(items,index) in myLists" :key="index" :index="items.path">
        {{ items.name }}
      </el-menu-item>
      <!-- <el-submenu v-for="(item,i) in navList" :key="i" v-show="item.second" :index="item.name">
        <template slot="title">{{ item.navItem }}</template>
        <el-menu-item v-for="(sec,j) in item.second" :key="j" :index="sec.name">{{ sec.navItem }}</el-menu-item>
      </el-submenu> -->
    </el-menu>
    <!-- <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <template slot="title">选项4</template>
              <el-menu-item index="1-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>导航二</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="2-1">选项1</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="2-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i>导航三</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="3-1">选项1</el-menu-item>
              <el-menu-item index="3-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="3-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="3-4">
              <template slot="title">选项4</template>
              <el-menu-item index="3-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>
    </el-container> -->
    <div class="back text-center"><router-link :to="{path: '/'}">返回首页</router-link></div>
  </div>
</template>

<script>
export default {
  props: ['myLists'],
  data () {
    return {

    }
  },
  // 路径及按键操作时调用
  updated () {
  // this.updateForcus()
  },
  // 会在F5刷新或第一次访问时被调用
  mounted () {
  // this.updateForcus()
  },
  methods: {
    // 修改导航active的两种方式，通过获取route的path参数来修改当前项
    updateForcus () {
      let path = this.$route.path
      if (path === '/my/myinfo') {
        this.navselected = '/my/myinfo'
      } else if (path === '/my/study') {
        this.navselected = 'my/study'
      }
    }
  }
}
</script>

<style lang="less">
// 这个去掉scoped，改成全局属性，是为了全局修改element-ui侧边栏的整体样式
.el-menu{
  background: none;
  border-right: none;
  .el-submenu{
    .el-submenu__title{
      color: @font-white;
      &:hover{
        background: none;
      }
    }
    .el-menu-item{
      color: @font-white;
    }
  }
  .el-menu-item{
    font-size: 16px;
    color: @font-white;
    text-align: center;
    height: 20px;
    line-height: 20px;
    padding-bottom: 32px;
    &:hover{
      background-color: RGBA(27, 31, 43, .8);
    }
    &:focus{
      background-color: RGBA(27, 31, 43, .2);
    }
  }
}
// 修改导航选中后的样式
.el-menu-item.is-active {
  color: @blue;
}
</style>

<style lang="less" scoped>
.sidebar-container{
  width: 12.5%;
  height: 100%;
  background: #1B1F2B;
  .logo{
    width: 72.5%;
    margin: auto;
    padding-top: 44px;
    img{
      width: 100%;
    }
  }
  .avatar{
    width: 50%;
    // 高度暂时写死
    height: 90px;
    background: @bg-white;
    border-radius: 50%;
    margin-top: 26px;
    margin-bottom: 26px;
  }
  .back{
    color: @font-white;
    font-size: 16px;
    // padding-bottom: 36px;
    position: fixed;
    bottom: 32px;
    left: 4%;
  }
}
</style>
