<template>
  <div id="index" class="index-page">
    <div class="plate-header">
      <header-block></header-block>
    </div>
    <div class="poster">
      <swiper-block></swiper-block>
    </div>
    <div class="section">
      <div class="container">
        <div class="title text-center">
          <div class="content">
            <img src="../assets/images/icon/blue.png"/>
            <p>精品课程训练营</p>
            <img src="../assets/images/icon/blue.png"/>
          </div>
        </div>
        <training-course :courseData = 'trainingCourse'></training-course>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div class="title text-center">
          <div class="content">
            <img src="../assets/images/icon/purple.png"/>
            <p>高级课程训练营</p>
            <img src="../assets/images/icon/purple.png"/>
          </div>
        </div>
        <high-level :courseData = 'highCourse'></high-level>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div class="title text-center">
          <div class="content">
            <img src="../assets/images/icon/green.png"/>
            <p>基础入门精品课</p>
            <img src="../assets/images/icon/green.png"/>
          </div>
        </div>
        <start-course :courseData = 'startCourse'></start-course>
      </div>

    </div>
    <div class="section teacher">

      <div class="container">
        <div class="title text-center">
          <p>我们的师资团队</p>
        </div>
        <teacher-info></teacher-info>
      </div>
    </div>
    <div class="teacher-bg">
      <img src="../assets/images/icon/Bg.png" />
    </div>
    <div class="section weare">
      <div class="container">
        <div class="title text-center">
          <p>人工只能+在线教育：我们是教育行业的变革者</p>
        </div>
        <we-are></we-are>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderBlock from '../components/header'
import SwiperBlock from '../components/swiper'
import HighLevel from '../components/course/highLevel'
import StartCourse from '../components/course/start'
import TrainingCourse from '../components/course/training'
import TeacherInfo from '../pages/default/teacher'
import WeAre from '../pages/default/weare'

export default {
  components: {
    HeaderBlock,
    SwiperBlock,
    HighLevel,
    StartCourse,
    TrainingCourse,
    TeacherInfo,
    WeAre
  },
  data () {
    return {
      trainingCourse: [],
      highCourse: [],
      startCourse: []
    }
  },
  created () {
    this.$axios.post('/api/index', {
    }).then(res => {
      this.trainingCourse = res.data.trainingcourses
      this.highCourse = res.data.heighcourses
      this.startCourse = res.data.startcourses
    }).catch(err => {
      console.log('数据异常', err)
    })
  }
}
</script>

<style lang="less" scoped>
.index-page{
  width: 100%;
}
.plate-header{
  position: absolute;
  width: 100%;
  height: 60px;
  background: #ffffff;
  box-shadow: 2px 2px 2px rgba(220,236,251,.7);
}
.poster{
  position: relative;
  height: @poster-height;
}
.section{
  margin-top: 60px;
  position: relative;
  z-index: 10;
  .container{
    width: @main-width;
    margin: auto;
  }
  .title{
    color: @gray;
    font-size: 20px;
    .content{
      height: 40px;
      line-height: 40px;
      img{
        display: inline-block;
        vertical-align: middle;
      }
      p{
        display: inline-block;
        vertical-align: middle;
        padding: 0 10px;
      }
    }
  }
}
.teacher-bg{
  width: 100%;
  position: absolute;
  bottom: 450px;
  img{
    width: 100%;
  }
}
.weare{
  // 设置底部渐变色
  background: linear-gradient(0.99turn, rgba(226,235,252,.6), rgba(226,235,252,0) 15%);
}
</style>
