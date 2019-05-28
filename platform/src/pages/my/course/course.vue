<template>
  <div class="my">
    <side-bar :myLists = 'myLists' :subTitle = 'false' @childHanandler='child' ></side-bar>
    <div class="right-container">
      <div class="aside-main-width ">
        <div class="course-top">
          <p class="plan">默认教学计划</p>
          <div class="courseinfo">
            <div class="progress">
                <canvas-circle :percent="percent"></canvas-circle>
              </div>
            <div class="main-content">
              <div class="course-progress">
              </div>
              <div class="items">
                <div class="item">
                  <div class="line1">
                    <i class="el-icon-success"></i>
                    <span>已完成</span>
                  </div>
                  <p class="item-cont"><span class="already">{{ finishTaskNum }}</span>/{{ allTaskNun }} <span>任务</span></p>
                </div>
                <div class="item">
                  <div class="line1">
                    <i class="el-icon-date"></i>
                    <span>学习有效期</span>
                  </div>
                  <p class="item-cont">2020-12-31</p>
                </div>
                <div class="item">
                  <div class="line1">
                    <i class="el-icon-document"></i>
                    <span>下一学习任务</span>
                  </div>
                  <p class="item-cont">{{ nextCatalogTitle }}</p>
                </div>
              </div>
              <button class="btn"><router-link :to="{path: '/mytask', query: {courseId: courseId, catalogId: nextCatalogId}}">继续学习</router-link></button>
            </div>
          </div>
        </div>
      </div>
      <div class="aside-main-width">
        <div class="course-content">
          <div class="chapter" :class="{active: currentIndex === index}" v-for="(item,index) in myLists" :key="index">
            <div class="top">
              <p class="number">第{{ index+1 }}章</p>
              <p class="name">{{ item.title|chaptorSlice }}</p>
              <p class="type">{{ item.label }}</p>
            </div>
            <p class="content">{{ item.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from '../../../components/side-bar-course'
import CanvasCircle from '../../../components/canvasCircle'
export default {
  components: {
    SideBar,
    CanvasCircle
  },
  data () {
    return {
      currentIndex: 0,
      courseId: '',
      // 学习进度
      percent: '',
      // 已完成任务数
      finishTaskNum: '',
      // 总任务数
      allTaskNun: '',
      // 下一学习任务
      nextCatalogTitle: '',
      nextCatalogId: '',
      // 课程信息
      myLists: []
    }
  },
  created () {
    let userId = sessionStorage.userId
    let courseId = location.href.split('?')[1].split('=')[1]
    this.courseId = courseId
    this.$axios.post('/api/course/getusercourse', {
      params: {
        courseid: courseId,
        userid: userId
      }
    }).then(res => {
      console.log(res)
      this.myLists = res.data.catalogs
      this.percent = res.data.course.dopercent
      this.finishTaskNum = res.data.overnum
      this.allTaskNun = res.data.tasknum
      this.nextCatalogTitle = res.data.nextcatalog.title
      this.nextCatalogId = res.data.nextcatalog.id
    }).catch(err => {
      console.log(err)
    })
  },
  methods: {
    child (index) {
      this.currentIndex = index
    }
  },
  filters: {
    chaptorSlice (val) {
      return val.split('：')[1]
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
  background: #F5F8FA;
  width: 87.5%;
}
.course-top{
  padding: 15px;
  .plan{
    font-size: 24px;
    color: @gray-dark;
  }
  .courseinfo{
    background-color: #fafafa;
    padding: 33px 15px;
    margin: 65px -15px 20px;
    .progress{
      position: absolute;
      top: 134px;
      width: 150px;
      height: 150px;
      background: #fff;
      border-radius: 50%;
      box-shadow: 0px 0px 18px 2px rgba(41,94,64,.1);
    }
    .main-content{
      width: 100%;
      // 清除float的影响
      overflow: hidden;
      .course-progress{
        width: 20%;
        height: 56px;
        float: left;
        position: relative;
      }
      .items{
        width: 66%;
        float: left;
        .item{
          display: inline-block;
          width: 32%;
          // 任务数量字体间隔扩大
          &:first-child{
            .item-cont{
              letter-spacing: 2px;
            }
          }
          .line1{
            color: @gray-darker;
            margin-bottom: 15px;
          }
          .item-cont{
            font-size: 16px;
            color: @gray-mider;
            .already{
              color: @blue;
            }
          }
        }
      }
      .btn{
        float: left;
        background: @blue;
        border: 1px solid @blue;
        color: @font-white;
        border-radius: 4px;
        width: 94px;
        height: 32px;
        margin-top: 12px;
      }
    }
  }
}
.course-content{
  padding: 20px;
  padding-bottom: 40px;
  position: relative;
  .chapter{
    padding-bottom: 70px;
    padding-left: 32px;
    border-left: 1px solid @blue;
    // 把第一个模块突出来的竖线隐藏掉
    &:first-child{
      &:before{
        content: '';
        display: inline-block;
        border-left: 1px solid @bg-white;
        position: absolute;
        left: 20px;
        height: 13px;
      }
    }
    &:last-child{
      padding-bottom: 0;
    }
    .top{
      font-size: 0;
      position: relative;
      .number{
        display: inline-block;
        font-size: 14px;
        background: @blue;
        color: @font-white;
        padding: 6px 12px;
        &:before{
          content: '';
          display: inline-block;
          border-bottom: 1px solid @blue;
          width: 32px;
          position: absolute;
          left: -32px;
          top: 13px;
        }
        &:after{
          content: '';
          display: inline-block;
          position: absolute;
          width: 0;
          height: 0;
          border-left: 13px solid @blue;
          border-top: 13px solid transparent;
          border-bottom: 13px solid transparent;
          left: 60px;
          top: 0px;
        }
      }
      .name{
        display: inline-block;
        font-size: 18px;
        color: @gray;
        padding: 0 20px;
      }
      .type{
        display: inline-block;
        height: 22px;
        line-height: 22px;
        color: @gray-mid;
        font-size: 14px;
        background: #fff2f2;
        padding: 0 14px;
        border-radius: 12px;
      }
    }
    .content{
      color: @gray-mider;
      font-size: 14px;
      line-height: 22px;
      padding-top: 32px;
      padding-left: 80px;
    }
  }
  .active{
    background: #eff7ff;
  }
}
</style>
