<template>
  <div>
    <p class="title">贪心科技旗下的贪心学院通过人工智能技术，打造最懂用户的自适应学习平台，为每一位用户提供个性化的职业教育服务。我们追求最精炼的AI教育内容和个人量身定制的课堂。</p>
    <div class="content">
      <div class="lf">
        <div class="row-top">
          <div class="rt-lf">
            <p class="connect">联系方式</p>
            <p class="detail">邮箱：info@greedyai.com</p>
            <p class="detail">地址：北京市朝阳区佳美中心写字楼</p>
          </div>
          <div class="rt-rt">
            <img class="big-img" src="../../assets/images/icon/gzhcode.png" />
            <img class="sm-img" src="../../assets/images/icon/zhi.png" />
            <img class="sm-img" src="../../assets/images/icon/CSDN.png" />
            <img class="sm-img" src="../../assets/images/icon/microblog.png" />
          </div>
        </div>
        <div class="row-bottom">
          <p>北京贪心科技有限公司  京ICP备18022135号-1</p>
        </div>
      </div>
      <div class="rt">
        <img src="../../assets/images/icon/map.png" />
        <div class="round china"></div>
        <div class="round american"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  }
}
</script>

<style lang="less" scoped>
.title{
  color: @gray-blue;
  font-size: 16px;
  width: 56%;
  margin: auto;
  line-height: 26px;
  padding-top: 30px;
}
.content{
  width: 100%;
  padding: 50px 0;
  overflow: hidden;
  .lf{
    width: 50%;
    float: left;
    padding-top: 20px;
    .row-top{
      width: 100%;
      height: 90px;
      padding-bottom: 40px;
      border-bottom: 1px solid @gray-blue;
      .rt-lf{
        width: 50%;
        float: left;
        .connect{
          color: @gray;
          font-size: 16px;
          padding-top: 10px;
        }
        .detail{
          font-size: 13px;
          color: @gray-blue;
          padding-top: 20px;
        }
      }
      .rt-rt{
        width: 50%;
        float: left;
        .big-img{
          width: 90px;
        }
        .sm-img{
          width: 30px;
          height: 30px;
          margin-bottom: 30px;
          padding-left: 16px;
        }
      }
    }
    .row-bottom{
      font-size: 13px;
      color: @gray-blue;
      padding-top: 40px;
    }
  }
  .rt{
    width: 50%;
    float: left;
    position: relative;
    .round{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #fd2259;
      position: absolute;
      &::after{
        content: '';
        border-radius: 50%;
        position: absolute;
        background: rgba(253, 34, 89, .4);
        animation: shine 2s ease-in-out 0.5s infinite normal;
      }
    }
    @keyframes shine {
      0% {
        width: 0px;
        height: 0px;
        border-radius: 50%;
        left: 5px;
        top: 5px;
      }
      100%{
        width: 16px;
        height: 16px;
        border-radius: 50%;
        left: -3px;
        top: -3px;
      }
    }
    .china{
      top: 64px;
      left: 42px;
    }
    .american{
      top: 70px;
      right: 126px;
    }
  }
}
</style>
