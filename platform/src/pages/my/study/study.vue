<template>
  <div class="">
    <div class="aside-main-width">
      <my-course :courseLists = 'courseLists' :tags = 'tags'></my-course>
    </div>
    <div class="aside-main-width">
      <my-course :courseLists = 'courseLists' :tags = 'tagsjoin'></my-course>
    </div>
  </div>
</template>

<script>
import MyCourse from '../../../components/course/my-course'
export default {
  components: {
    MyCourse
  },
  data () {
    return {
      tags: '学习中',
      tagsjoin: '加入的课程',
      courseLists: []
      // courseLists: [
      //   {
      //     title: '知识图谱入门班',
      //     percent: 13
      //   },
      //   {
      //     title: '深度学习入门班',
      //     percent: 16
      //   }
      // ]
    }
  },
  created () {
    this.$axios.post('/api/user/getallcourse', {
      params: {
        userid: sessionStorage.userId
      }
    }).then(res => {
      console.log(res.data.courses)
      this.courseLists = res.data.courses
    }).catch(err => {
      console.log('获取课程信息失败' + err)
    })
  }
}
</script>

<style lang="less" scoped>

</style>
