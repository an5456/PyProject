<template>
  <div class="container">
    <div class="section-title">
      <p class="text-center">{{ title }}</p>
    </div>
    <div class="items">
      <div class="item" v-for="(item,index) in lists" :key="index">
        <div class="itemimg"><img class="center-block" :src="item.imgsrc" /></div>
        <p class="info text-center">{{ item.info }}</p>
        <p class="content">{{ item.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '纯职业导向，步入升职加薪的捷径',
      lists: [
        {
          // 用require请求图片地址，在webpack中会将图片图片来当做模块来用，因为是动态加载的，所以url-loader将无法解析图片地址，然后npm run dev 或者npm run build之后导致路径没有被加工
          // require之后可以把图片当作模块加载进去
          imgsrc: require('../../assets/images/course-introduce/icons/plateform.png'),
          info: '实践比理论更重要',
          content: '完成本课程，你将积累丰富的项目实操经验。我们的课程由多个实战项目组成，设计了能够夯实基础知识、具有超强针对性的实操训练。我们不仅仅培养学员的算法能力跟工程能力，还保证学员能够“学完之后真的能做出来”。'
        },
        {
          imgsrc: require('../../assets/images/course-introduce/icons/chatbot.png'),
          info: '选择比努力更重要',
          content: '在我们个性化项目式课程中积累的宝贵经验将帮助你完善简历和提高面试通过率。贪心科技与国内尖端AI公司达成深度合作，力求为学员进行定向实习与工作推荐。'
        },
        {
          imgsrc: require('../../assets/images/course-introduce/icons/ren.png'),
          info: '机遇比学历更重要',
          content: '通过本课程，你将与来自各大公司的同学和行业一线导师结交，积累自己的人脉、洞察行业发展趋势、明确职业发展方向、突破自己职业发展的瓶颈。'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.items{
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  padding: 0 30px;
  .item{
    width: 260px;
    float: left;
    .itemimg{
      height: 47px;
    }
    .info{
      width: 184px;
      height: 34px;
      line-height: 34px;
      color: @font-white;
      background: @blue-lighter;
      margin: auto;
      border-radius: 18px;
      margin-bottom: 22px;
      margin-top: 10px;
    }
    .content{
      font-size: 14px;
      color: @font-white;
      line-height: 20px;
    }
  }
}
</style>
