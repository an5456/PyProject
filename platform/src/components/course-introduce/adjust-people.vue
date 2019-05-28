<template>
  <div class="container">
    <div class="section-title">
      <p class="text-center">{{ title }}</p>
    </div>
    <div class="item" v-for="(item,index) in adjustPeople" :key="index">
      <p class="letter">{{ item.letter }}</p>
      <div class="detaile"><p>{{ item.content }}</p></div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '适合什么样的人群',
      adjustPeople: [
        {
          letter: 'A',
          content: '希望从事人工智能Python开发等工作；'
        },
        {
          letter: 'B',
          content: '未来想继续在AI领域深造的学员；'
        },
        {
          letter: 'C',
          content: '有数据分析工程师、爬虫工程师等工作岗位申请需求的学员；'
        },
        {
          letter: 'D',
          content: '急需通过企业级实操项目丰富简历及提高面试通过率的学员；'
        },
        {
          letter: 'E',
          content: '对现状不满，对人生“贪心”，想要升职加薪、当上总经理、出任CEO'
        }
      ]
    }
  }
}
</script>

<style lang="less" scoped>
.section-title{
  padding-bottom: 70px;
}
.item{
  width: 560px;
  height: 38px;
  line-height: 38px;
  margin: auto;
  font-size: 0;
  margin-bottom: 15px;
  &:last-child{
    margin-bottom: 0;
  }
  .letter{
    width: 20px;
    height: 38px;
    line-height: 38px;
    display: inline-block;
    color: @blue-lighter;
    font-size: 28px;
    padding-right: 10px;
    position: relative;
    top: 4px;
  }
  .detaile{
    display: inline-block;
    width: 522px;
    height: 36px;
    line-height: 36px;
    font-size: 14px;
    color: @font-white;
    border: 1px solid @blue-lighter;
    p{
      padding: 0 30px;
    }
  }
}
</style>
