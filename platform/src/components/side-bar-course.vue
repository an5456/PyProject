<template>
  <div class="sidebar-container">
    <div class="logo">
      <img src="../assets/images/icon/logo.png" />
    </div>
    <div class="avatar center-block">
    </div>
    <!-- 递归组件的时候在ul中做循环，有子菜单 -->
    <ul class="sidebar-ul" v-for="(item, index) in myLists" :key="index" v-if="subTitle">
      <tree :model="item" :chaptorId = "index" @videotitle = "videotitle"></tree>
    </ul>
    <!-- 只有一个目录的情况 -->
    <ul class="sidebar-ul" v-if="!subTitle">
      <li
        class="sidebar-li text-center"
        :class="{active: currentIndex === index}"
        v-for="(items,index) in myLists" :key="index"
        @click="clickChapter(index)">
        {{ items.title }}
      </li>
    </ul>
    <!-- <ul class="sidebar-ul">
      <li v-if="!subTitle"
        class="sidebar-li text-center"
        :class="{active: currentIndex === index}"
        v-for="(items,index) in myLists" :key="index"
        @click="clickChapter(index)">
        {{ items.title }}
      </li>
      <li class="sidebar-li" v-if="subTitle" v-for="(items,index) in myLists" :key="index" >
        <div @click="showToggle(items)">{{ items.title }}</div>
        <ul v-if="items.sections.length > 0" v-show="showSubCaptor" >
          <li v-for="(subitems, subid) in items.sections" :key="subid" @click="showToggle(items, subitems)">
            <div>{{subitems.title}}</div>
          </li>
        </ul>
      </li>
    </ul> -->
    <!-- <template v-for="list in this.myLists">
      <el-submenu index="1" v-if="list.sections.length > 0" :key="list.id" :index="list.title">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span slot="title">{{ list.title}}</span>
        </template>
        <SideBar :myLists="list.sections"></SideBar>
      </el-submenu>
      <el-menu-item v-else :key="list.id" :index="list.title">
        <span>{{ list.title}}</span>
      </el-menu-item>
    </template> -->
    <div class="back text-center"><router-link :to="{path: '/'}">返回首页</router-link></div>
  </div>
</template>

<script>
import Tree from '../components/side-bar-course-item'

export default {
  props: ['myLists', 'subTitle'],
  components: {
    Tree
  },
  data () {
    return {
      currentIndex: 0,
      showSubCaptor: false
    }
  },
  methods: {
    clickChapter (index) {
      this.currentIndex = index
      this.$emit('childHanandler', index)
    },
    clickOption (index) {
      console.log(index)
      this.showSubCaptor = !this.showSubCaptor
    },
    videotitle (title, videoSrc) {
      console.log(title)
      this.$emit('videoInfo', title, videoSrc)
    }
  }
}
</script>

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

  .sidebar-li{
    color: @font-white;
    padding: 5px;
    font-size: 14px;
    cursor: pointer;
  }
  .active{
    color: @blue;
  }

}
</style>
