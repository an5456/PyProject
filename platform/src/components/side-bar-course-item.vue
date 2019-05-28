<template>
  <li class="sidebar-li">
    <div @click="toggle(chaptorId)">
      <!-- <span v-if='!isFolder'><i class="el-icon-document"></i>第{{chaptorId + 1}}章：{{ model.title }}</span>
      <span v-if='isFolder'>{{chaptorId + 1}}：{{ model.title }}</span> -->
      <i class="el-icon-document" v-if="isFolder"></i>{{ model.title }}
    </div>
    <ul v-show="open" v-if="isFolder" class="sub-ul">
      <items v-for='(cel, celid) in model.sections' :model='cel' :chaptorId='celid' :key='cel.id'></items>
    </ul>
  </li>
</template>

<script>
export default {
  name: 'items',
  props: ['model', 'chaptorId'],
  data () {
    return {
      open: false
    }
  },
  computed: {
    isFolder () {
      return this.model.sections && this.model.sections.length
    }
  },
  methods: {
    toggle (chaptorId) {
      if (this.isFolder) {
        this.open = !this.open
      }
      let userId = sessionStorage.userId
      let courseId = location.href.split('?')[1].split('&')[0].split('=')[1]
      this.courseId = courseId
      this.$axios.post('/api/course/play', {
        params: {
          courseid: courseId,
          userid: userId,
          catalogid: this.model.id
        }
      }).then(res => {
        console.log(res)
        // if (res.data.video[0].type === 'section') {
        //   this.title = res.data.video[0].title
        //   this.videoSrc = res.data.video[0].video.video
        // } else {
        //   this.title = res.data.video[0].title
        //   this.videoSrc = ''
        // }
        this.title = res.data.video[0].title
        this.videoSrc = res.data.video[0].video.video
        this.$store.commit('changeVideoSrc', this.videoSrc)
        this.$store.commit('changeVideoTitle', this.title)
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style lang="less" scoped>
.sidebar-li{
  color: @font-white;
  padding: 5px 0;
  font-size: 14px;
  cursor: pointer;
  padding-left: 16px;
  line-height: 20px;
}
.sub-ul{
  padding-top: 5px;
}
</style>
