<template>
  <div class="order">
    <div class="container">
      <div class="header">
        <router-link to="/"><img src='../../assets/images/icon/logobule.png' /></router-link>
      </div>
      <div class="box">
        <p class="time">请在15分钟内完成支付；我们以为您预定了本期班级席位；</p>
        <div class="order-content">
          <div class="title">订单详情</div>
          <div class="course-info">
            <p class="name">{{ courseName }}</p>
            <p class="starttime">{{ startTime }}开课</p>
          </div>
          <div class="line"></div>
          <div class="price">¥{{ price }}</div>
          <div class="line"></div>
          <div class="buybtn">
            <button class="btn">提交订单</button>
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
      courseName: '初级机器学习训练营',
      startTime: '3月13日',
      price: 6998
    }
  }
}
</script>

<style lang="less" scoped>
.order{
  background: #f2f2f2;
  padding: 92px 0;
  width: 100%;
  .header{
    padding-bottom: 46px;
  }
  .box{
    width: 1090px;
    padding-left: 30px;
    .time{
      color: @red;
      font-size: 14px;
      padding-bottom: 34px;
    }
    .order-content{
      width: 100%;
      height: 496px;
      background: @bg-white;
      border-radius: 4px;
      margin: auto;
      .title{
        height: 54px;
        line-height: 54px;
        background: #F5FBFF;
        color: @gray-mid;
        border-radius: 2px 2px 0px 0px;
        padding-left: 8px;
      }
      .course-info{
        color: @gray-dark;
        font-size: 20px;
        padding: 46px 0;
        padding-left: 8px;
        .name{
          display: inline-block;
          padding-right: 324px;
        }
        .starttime{
          display: inline-block;
        }
      }
      .line{
        width: 1040px;
        height: 1px;
        background: #dcdcdc;
        margin: auto;
      }
      .price{
        color: @red;
        font-size: 20px;
        height: 60px;
        line-height: 60px;
        padding-left: 950px;
      }
      .buybtn{
        overflow: hidden;
        padding-right: 32px;
        padding-top: 114px;
        .btn{
          float: right;
          width: 120px;
          height: 40px;
          line-height: 40px;
          color: @font-white;
          background: @blue-lighter;
          border: @blue-lighter;
          border-radius: 4px;
          font-size: 14px;
          cursor: pointer;
          &:focus{
            // 点击按钮之后消除包裹按钮周围的线条
            outline: 0px;
          }
        }
      }
    }
  }

}
</style>
