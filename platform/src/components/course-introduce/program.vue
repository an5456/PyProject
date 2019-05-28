<template>
  <div class="program">
    <div class="container">
      <div class="section-title">
        <p class="text-center">{{ lists.length }}大项目带你飞</p>
      </div>
      <div class="item" v-for="(item,index) in lists" :key="index">
        <div class="lf">
          <img :src="item.pic" />
        </div>
        <div class="rt">
          <p class="title">{{ item.title }}</p>
          <p class="intro">{{ item.content }}</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // lists: [
      //   {
      //     // 用require请求图片地址，在webpack中会将图片图片来当做模块来用，因为是动态加载的，所以url-loader将无法解析图片地址，然后npm run dev 或者npm run build之后导致路径没有被加工
      //     // require之后可以把图片当作模块加载进去
      //     img: require('../../assets/images/course-introduce/mechine-learning/item1.png'),
      //     name: '广告点击率预测项目（CTR）',
      //     intro: '基本上很多的互联网企业的主要收入来自于广告。其中对收入影响最大的就是广告的点击率，而且需要根据预测的点击率来优化广告列表的展示。'
      //   },
      //   {
      //     img: require('../../assets/images/course-introduce/mechine-learning/item2.png'),
      //     name: '情感分析项目(sentiment analysis)',
      //     intro: '在文本分析领域，情感分析是应用场景最为广泛的技术。在此项目中，我们结合分类算法以及各类特征工程技术来搭建基于评论的情感分析系统。'
      //   },
      //   {
      //     img: require('../../assets/images/course-introduce/mechine-learning/item3.png'),
      //     name: '金融风控预测项目(credit risk prediction)',
      //     intro: '在金融科技领域，风控是核心。在此项目中，我们需要搭建一个风控系统，此系统可以帮助我们更好地管理用户的风险，从而更准确地做放贷与否的决策。'
      //   },
      //   {
      //     img: require('../../assets/images/course-introduce/mechine-learning/item4.png'),
      //     name: '推荐系统项目',
      //     intro: '这是一个开放性项目，学员选择方向以及题目，导师及助教团队全程指导你完成。所选项目可以围绕着自己所熟悉和希望探索的任何Python开发场景。任何创新的项目，你想要尝试但无法在工作岗位上做的项目，都可以在这个项目中得到架构及实践的机会。'
      //   },
      //   {
      //     img: require('../../assets/images/course-introduce/mechine-learning/item5.png'),
      //     name: '图像识别项目',
      //     intro: '在本项目中，我们利用卷积神经网络模型来实现交通牌的识别。由于噪声的影响，这个问题拥有很大的挑战。'
      //   }
      // ]
    }
  },
  props: ['lists']
}
</script>

<style lang="less" scoped>
.section-title{
  padding-bottom: 80px;
}
.program{
  .item{
    width: 100%;
    overflow: hidden;
    margin-bottom: 50px;
    background: #131d31;
    border-radius: 10px;
    box-shadow: 2px 10px 20px -2px rgba(57,118,241,.22);
    &:last-child{
      margin-bottom: 0;
    }
    .lf{
      float: left;
      width: 290px;
      img{
        width: 100%;
      }
    }
    .rt{
      float: left;
      width: 71%;
      padding: 0 20px;
      .title{
        font-size: 16px;
        color: #3976f1;
        padding-top: 40px;
      }
      .intro{
        font-size: 14px;
        color: @font-white;
        line-height: 20px;
        padding-top: 24px;
      }
    }
  }
}
</style>
