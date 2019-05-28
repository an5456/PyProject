<template>
  <div class="team">
    <div class="container">
      <div class="section-title">
        <p class="text-center">{{ title }}</p>
      </div>
      <div class="teamdetail">
        <ul>
          <li v-for="(item,index) in teacherInfo" :key="index">
            <div class="item">
              <img class="imginfo" :src="item.imgsrc" />
              <p class="position">{{ item.position }}</p>
              <p class="intro">{{ item.intro }}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '研发团队',
      teacherInfo: [
        {
          // 用require请求图片地址，在webpack中会将图片图片来当做模块来用，因为是动态加载的，所以url-loader将无法解析图片地址，然后npm run dev 或者npm run build之后导致路径没有被加工
          // require之后可以把图片当作模块加载进去
          imgsrc: require('../../assets/images/course-introduce/teacher/zhou.png'),
          position: '贪心学院科技副院长',
          intro: '周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深工程师、多家一线公司技术负责人和技术顾问。业内公认的技术工程、数据分析、大数据等多领域专家。曾参与百度人工智能开放平台计算机视觉板块AI模型的设计与研发，领导百度图像识别项目技术团队完成百度AI图像识别从零开始的技术积累。主导并研发了行业首个知识图谱金融风控项目并任技术负责人，带领团队搭建了国内首家服务于金融领域的实时风控模型，并在企业中得到广泛应用。'
        },
        {
          imgsrc: require('../../assets/images/course-introduce/teacher/zhou.png'),
          position: '贪心学院科技副院长',
          intro: '周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深工程师、多家一线公司技术负责人和技术顾问。业内公认的技术工程、数据分析、大数据等多领域专家。曾参与百度人工智能开放平台计算机视觉板块AI模型的设计与研发，领导百度图像识别项目技术团队完成百度AI图像识别从零开始的技术积累。主导并研发了行业首个知识图谱金融风控项目并任技术负责人，带领团队搭建了国内首家服务于金融领域的实时风控模型，并在企业中得到广泛应用。'
        },
        {
          imgsrc: require('../../assets/images/course-introduce/teacher/zhou.png'),
          position: '贪心学院科技副院长',
          intro: '周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深工程师、多家一线公司技术负责人和技术顾问。业内公认的技术工程、数据分析、大数据等多领域专家。曾参与百度人工智能开放平台计算机视觉板块AI模型的设计与研发，领导百度图像识别项目技术团队完成百度AI图像识别从零开始的技术积累。主导并研发了行业首个知识图谱金融风控项目并任技术负责人，带领团队搭建了国内首家服务于金融领域的实时风控模型，并在企业中得到广泛应用。'
        },
        {
          imgsrc: require('../../assets/images/course-introduce/teacher/zhou.png'),
          position: '贪心学院科技副院长',
          intro: '周景阳，贪心科技（Greedy Technology）技术合伙人、人工智能领域专家、百度人工智能事业群资深工程师、多家一线公司技术负责人和技术顾问。业内公认的技术工程、数据分析、大数据等多领域专家。曾参与百度人工智能开放平台计算机视觉板块AI模型的设计与研发，领导百度图像识别项目技术团队完成百度AI图像识别从零开始的技术积累。主导并研发了行业首个知识图谱金融风控项目并任技术负责人，带领团队搭建了国内首家服务于金融领域的实时风控模型，并在企业中得到广泛应用。'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.team{
  .section-title{
    padding-bottom: 100px;
  }
  .teamdetail{
    position: relative;
    overflow-x: scroll;
    ul{
      overflow: hidden;
      width: 1300px;
      padding-top: 60px;
      li{
        width: 320px;
        float: left;
        .item{
          width: 300px;
          height: 465px;
          border: 1px solid #3976f1;
          background: #131d31;
          border-radius: 3px;
          .imginfo{
            display: block;
            margin-left: auto;
            margin-right: auto;
            position: relative;
            top: -59px;
          }
          .position{
            background: #3976f1;
            border-radius: 3px;
            width: 156px;
            height: 30px;
            line-height: 30px;
            text-align: center;
            margin: auto;
            color: @font-white;
            font-size: 14px;
            position: relative;
            top: -40px;
          }
          .intro{
            font-size: 14px;
            color: @font-white;
            padding: 0 10px;
            line-height: 20px;
          }
        }
      }
    }
  }
}
</style>
