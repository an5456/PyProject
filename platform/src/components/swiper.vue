<template>
  <div>
    <swiper :options = "swiperOption">
      <swiper-slide class="swiper-img">I'm Slide 1</swiper-slide>
      <swiper-slide class="swiper-img">I'm Slide 2</swiper-slide>
      <swiper-slide class="swiper-img">I'm Slide 3</swiper-slide>
      <div class="swiper-pagination"  slot="pagination"></div>
    </swiper>
    <div class="swiper-box">
      <div class="slogen">
        <p class="detaile">这里放课程宣传标语</p>
        <p class="detaile">这里放课程课程宣传标语</p>
      </div>
      <div class="course">
        <div class="content">
          <img src="../assets/images/icon/star.png" />
          <p class="course-title">Course Title</p>
          <p class="course-intro">We can put one of the import class here</p>
          <p class="course-intro">We can put one of the import class here</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      swiperOption: {
        pagination: {
          el: '.swiper-pagination'
        },
        // 循环
        loop: true,
        // 设定初始化时slide的索引
        initialSlide: 0,
        // 自动播放
        autoplay: true,
        speed: 1000
      }
    }
  }
}
</script>

<style lang="less" scoped>
.swiper-img{
  background: #2e57b4;
  width: 100%;
  height: 570px;
}
.swiper-box{
  width: @main-width;
  position: relative;
  top: -570px;
  z-index: 10;
  height: 470px;
  margin: auto;
  .slogen{
    position: absolute;
    top: 140px;
    .detaile{
      font-size: 30px;
      color: @font-white;
    }
  }
  .course{
    width: 370px;
    height: 254px;
    border-radius: 22px;
    background: @bg-white;
    position: absolute;
    top: 130px;
    right: 40px;
    z-index: 10;
    .content{
      padding: 30px 20px;
      .course-title{
        color: @blue-dark;
        font-size: 20px;
        padding: 15px 0 20px 15px;
      }
      .course-intro{
        color: @blue-light;
        font-size: 16px;
        padding-left: 15px;
        padding-bottom: 10px;
        background: inherit;
      }
    }
  }
}
</style>
