<template>
  <div class="my">

    <side-bar :myLists = 'myLists' :subTitle = 'true'></side-bar>
    <!-- <el-menu
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      unique-opened
    >
      <SideBar :myLists = 'this.myLists'></SideBar>
    </el-menu> -->
    <div class="right-container">
      <p class="title text-center">{{ title }}</p>
      <my-video></my-video>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import SideBar from '../../../components/side-bar-course'
import MyVideo from '../../../components/my-video'

export default {
  components: {
    SideBar,
    MyVideo
  },
  data () {
    return {
      courseId: '',
      // title: '',
      // videoSrc: '',
      isCollapse: false, // 菜单展开功能
      myLists: [
        {
          title: '第一章：Python基础语法',
          capter_id: 3,
          id: 3,
          active: false,
          sections: [
            {
              title: '1.1 课程介绍',
              capter_id: 3,
              active: false,
              id: 10
            }
          ]
        },
        {
          title: '第二章：Python工程结构',
          capter_id: 4,
          id: 4,
          active: false,
          sections: [
            {
              title: '2.1工程结构与命名规范',
              capter_id: 4,
              active: false,
              id: 5
            },
            {
              title: '2.2模块与包',
              capter_id: 4,
              active: false,
              id: 6
            }
          ]
        },
        {
          title: '第三章：面向对象',
          capter_id: 5,
          id: 7,
          active: false,
          sections: [
            {
              title: '3.1什么是面向对象',
              capter_id: 5,
              active: false,
              id: 8
            },
            {
              title: '3.2构造函数',
              capter_id: 5,
              active: false,
              id: 9
            }
          ]
        }
      ]
    }
  },
  // computed: {
  //   cont () {
  //     return this.$store.state.taskVideoSrc
  //   },
  //   title () {
  //     return this.$store.state.taskVideoTitle
  //   }
  // },
  // computed: mapState({
  //   // 1.箭头函数
  //   cont: state => state.taskVideoSrc,
  //   // 2.传字符串参数’taskVideoSrc‘等同于state => state.taskVideoSrc
  //   coutLis: 'taskVideoSrc',
  //   title: state => state.taskVideoTitle
  // }),
  computed: {
    ...mapState({
      title: 'taskVideoTitle'
      // coutLis: 'taskVideoSrc',
      // title: state => state.taskVideoTitle
    })
  },
  created () {
    let userId = sessionStorage.userId
    let courseId = location.href.split('?')[1].split('&')[0].split('=')[1]
    let catalogId = location.href.split('?')[1].split('&')[1].split('=')[1]
    this.$axios.post('/api/course/play', {
      params: {
        courseid: courseId,
        userid: userId,
        catalogid: catalogId
      }
    }).then(res => {
      console.log(res)
      let title = res.data.video[0].title
      let videoSrc = res.data.video[0].video.video
      this.$store.commit('changeVideoTitle', title)
      this.$store.commit('changeVideoSrc', videoSrc)
    }).catch(err => {
      console.log('获取信息失败', err)
    })
  },
  methods: {
    toggleClick () {
      this.isCollapse = !this.isCollapse
    }
  }
}
</script>

<style lang="less" scoped>
.my{
  // 最低高度填满屏幕视口，如果div内容不够，则撑起div
  min-height: 100vh;
  width: 100%;
  display: flex;
}
.right-container{
  background: @bg-white;
  width: 87.5%;
  .title{
    color: @blue;
    font-size: 24px;
    font-family: PingFangSC-Regular;
    padding-top: 40px;
    padding-bottom: 20px;
  }
}
</style>
