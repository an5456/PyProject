<template>
  <div class="teacher">
    <div class="box">
      <div class="rectangle"></div>
      <div class="content">
        <div class="sm-item item">
          <div class="teacher-img"></div>
          <div class="teacher-top">
            <p class="author">周景阳</p>
            <p class="position">贪心学院教学副总裁</p>
          </div>
          <div class="teacher-intro">周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深</div>
        </div>
        <div class="lg-item item">
          <div class="teacher-img"></div>
          <div class="teacher-top">
            <p class="author">周景阳</p>
            <p class="position">贪心学院教学副总裁</p>
          </div>
          <div class="teacher-intro">周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深</div>
        </div>
        <div class="sm-item item">
          <div class="teacher-img"></div>
          <div class="teacher-top">
            <p class="author">周景阳</p>
            <p class="position">贪心学院教学副总裁</p>
          </div>
          <div class="teacher-intro">周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.teacher{
  padding-top: 60px;
  .box{
    position: relative;
    .rectangle{
      width: 990px;
      height: 205px;
      border-radius: 20px;
      margin: auto;
      background: linear-gradient(#3557b3,#658ff4);
    }
    .content{
      display: flex;
      justify-content: space-between;
      position: relative;
      top: -100px;
      .item{
        position: relative;
        width: 305px;
        border-radius: 20px;
        background: @bg-white;
        box-shadow: 2px 2px 20px rgba(50, 85, 177, 0.16);
        padding: 0 30px;
        display: inline-block;
        .teacher-img{
          background: #3557b3;
          border-radius: 50%;
          border: 4px solid #fff;
          position: absolute;
        }
        .teacher-top{
          padding-bottom: 25px;
          p{
            display: inline-block;
          }
          .author{
            font-size: 16px;
          }
          .position{
            float: right;
            font-size: 14px;
          }
        }
        .teacher-intro{
          color: @gray-darker;
          font-size: 14px;
          line-height: 24px;
          overflow: hidden;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          transition: all 0.5s ease;
        }
      }
      .lg-item{
        height: 215px;
        .teacher-img{
          width: 110px;
          height: 110px;
          left: 123.5px;
          top: -59px;
          transition: all 0.5s ease;
        }
        .teacher-top{
          padding-top: 80px;
          transition: all 0.5s ease;
        }
        &:hover{
          .teacher-img{
            width: 35px;
            height: 35px;
            left: 261px;
            top: -21.5px;
          }
          .teacher-top{
            padding-top: 41px;
          }
          .teacher-intro{
            overflow: visible;
            display: block;
            // -webkit-line-clamp: max;
          }
        }
      }
      .sm-item{
        height: 185px;
        .teacher-img{
          width: 35px;
          height: 35px;
          left: 161px;
          top: -21.5px;
        }
        .teacher-top{
          padding-top: 41px;
        }
      }
    }
  }
}
</style>
