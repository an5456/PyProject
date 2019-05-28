<template>
  <div>
    <div class="container">
      <div class="section-title">
        <p class="text-center">{{ title }}</p>
      </div>
      <div class="teacher">
        <div class="box">
          <div class="lf">
            <img  src="../../assets/images/course-introduce/teacher/zhou-big.png"/>
          </div>
          <div class="rt">
            <p class="name">周景阳</p>
            <div class="info">
              <p>-百度资深工程师</p>
              <p>-贪心科技硅谷AI联合项目负责人</p>
              <p>-国美金融技术负责人/架构师</p>
              <p>-凡普金科大数据中心技术负责人</p>
              <p>-8年以上AI方面的开发经验</p>
              <p>-多家教育平台金牌讲师，拥有学员10W+</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  data () {
    return {
      title: '导师介绍'
    }
  }
}
</script>

<style lang="less" scoped>
.teacher{
  width: 960px;
  height: 285px;
  margin: auto;
  background: #121b2e;
  box-shadow: 0px 8px 10px -2px rgba(25, 38, 65, 0.8);
  border-radius: 3px;
  .box{
    overflow: hidden;
    .lf{
      width: 400px;
      height: 285px;
      float: left;
      img{
        width: 100%;
      }
    }
    .rt{
      float: left;
      padding-left: 20px;
      .name{
        color: #3976f1;
        font-size: 30px;
        text-decoration: underline;
        padding: 30px 0 20px;
      }
      .info{
        color: @font-white;
        font-size: 16px;
        p{
          padding-bottom: 10px;
          line-height: 20px;
        }
      }
    }
  }
}
</style>
