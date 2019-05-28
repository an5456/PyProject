<!--课程介绍页面“大纲部分”-->
<template>
  <div class="chapter">
    <div class="container">
      <div class="section-title">
        <p class="text-center">{{ title }}</p>
      </div>
      <div v-for="(item, index) in lists" :key="index">
        <!-- :item传值给子组建，把list里的每一次循环的值传给子组件 -->
        <collapse-item :item = 'item' :indexs = 'index'></collapse-item>
      </div>
    </div>

  </div>
</template>

<script>
// 引入章节面板组件
import CollapseItem from '../collapse-item'
export default {
  components: {
    CollapseItem
  },
  data () {
    return {
      title: '课程大纲'
      // 大纲数据
      // lists: [
      //   {
      //     id: 0,
      //     name: 'Python基础语法',
      //     type: 'chapter',
      //     subChapter: [
      //     ]
      //   },
      //   {
      //     id: 1,
      //     name: 'Python工程结构',
      //     type: 'chapter',
      //     subChapter: [
      //       {
      //         id: 0,
      //         name: '工程结构与命名规范'
      //       },
      //       {
      //         id: 1,
      //         name: '模块与包'
      //       }
      //     ]
      //   },
      //   {
      //     id: 2,
      //     name: '搭建基于规则的ChatBot',
      //     type: 'program',
      //     subChapter: [
      //       {
      //         id: 0,
      //         name: 'Python编程风格'
      //       },
      //       {
      //         id: 1,
      //         name: '基本数据类型'
      //       }
      //     ]
      //   },
      //   {
      //     id: 3,
      //     name: 'Python基础语法',
      //     type: 'chapter',
      //     subChapter: [
      //       {
      //         id: 0,
      //         name: 'Python编程风格'
      //       },
      //       {
      //         id: 1,
      //         name: '基本数据类型'
      //       }
      //     ]
      //   }
      // ]
    }
  },
  props: ['lists']
}
</script>

<style lang="less" scoped>
.section-title{
  padding-bottom: 110px;
}
</style>
