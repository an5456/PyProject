<!--首页训练营课程-->
<template>
  <div class="course-list">
    <!--elementui 布局-->
    <el-row :gutter="20">
      <el-col :span="8" v-for="(item, index) in courseData" :key='index'>
        <div class="grid-content bg-purple course-item">
          <div class="course-img">
            <a v-if="item.url"><router-link :to="{ path: item.url, query: { courseId: item.id }}"><img :src="item.pic"></router-link></a>
            <a v-else><img :src="item.pic"></a>
          </div>
          <div class="course-info">
            <p class="subscribe" v-if="item.url"><router-link :to="{ path: item.url, query: { courseId: item.id }}">{{ item.content }}</router-link></p>
            <p class="subscribe" v-else>{{ item.content }}</p>
            <div class="detail">
              <p class="pretime">上期开课时间：{{ item.last_time }}<span>{{ item.isFull }}</span></p>
              <p class="nextime">下期开课时间：{{ item.next_time }}<span>仅剩{{ item.max_people_num }}位</span></p>
              <p class="price">¥{{ item.cost }} </p>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // courseData: [
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     preTime: '12月10日',
      //     nextTime: '4月7日',
      //     price: 16998,
      //     isFull: '已满',
      //     remainNum: 30
      //   },
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     preTime: '12月10日',
      //     nextTime: '4月7日',
      //     price: 16998,
      //     isFull: '已满',
      //     remainNum: 30
      //   },
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     preTime: '12月10日',
      //     nextTime: '4月7日',
      //     price: 16998,
      //     isFull: '已满',
      //     remainNum: 30
      //   }
      // ]
    }
  },
  // 接收index传过来的课程值
  props: ['courseData']

}
</script>

<style lang="less" scoped>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
// .bg-purple {
//   background: #d3dce6;
// }
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.course-item{
  box-shadow: 2px 2px 20px rgba(72,72,72,.16);
  margin-top: 45px;
  border-radius: 22px;
  &:hover{
    box-shadow: 2px 12px 14px -3px rgba(72, 72, 72, 0.16);
  }
  .course-img{
    height: 140px;
  }
  .course-info{
    height: 185px;
    padding: 0 30px;
    .subscribe{
      line-height: 24px;
      padding: 25px 0;
      font-size: 16px;
      height: 48px;
    }
    .detail{
      font-size: 14px;
      .pretime{
        padding-bottom: 14px;
        color: #4e4e4e;
        span{
          background: #f7edef;
          color: #ee3943;
          padding: 2px 4px;
          border-radius: 2px;
        }
      }
      .nextime{
        padding-bottom: 14px;
        color: #4e4e4e;
        span{
          color: #fff;
          background: #fc6d21;
          padding: 2px 4px;
          border-radius: 2px;
          margin-left: 4px;
          letter-spacing: 1px;
        }
      }
      .price{
        padding-right: 6px;
      }
    }
  }
}
</style>
