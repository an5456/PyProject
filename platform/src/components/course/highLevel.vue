<!--首页高级课程训练营-->
<template>
  <div class="course-list">
    <el-row :gutter="20">
      <el-col :lg="6" :md="4" :xs="12" v-for="(item, index) in courseData" :key='index'>
        <div class="grid-content bg-purple course-item">
          <div class="course-img">
            <a><router-link to="/info-machine-learning"><img :src="item.pic"></router-link></a>
          </div>
          <div class="course-info">
            <p class="subscribe">{{ item.content }}</p>
            <div class="detail">
              <p class="level">{{ item.level }}</p>
              <p class="price">¥<span>{{ item.cost }}</span></p>
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
      //     level: '高级',
      //     price: 16998
      //   },
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     level: '高级',
      //     price: 16998
      //   },
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     level: '初级',
      //     price: 16998
      //   },
      //   {
      //     subscribe: 'Python编程搭配数学基础，再你必备的AI基础课',
      //     level: '中级',
      //     price: 16998
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
    height: 130px;
    padding: 0 20px;
    .subscribe{
      font-size: 16px;
      line-height: 22px;
      padding: 25px 0;
    }
    .detail{
      color: #ea7e1e;
      p{
        display: inline-block;
      }
      .price{
        float: right;
        padding-right: 6px;
      }
    }
  }
}
</style>
