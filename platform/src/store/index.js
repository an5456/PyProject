import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

// 全局访问的state对象
const state = {
  // 给video一个默认的视频，解决页面第一次加载的时候videojs报错
  taskVideoSrc: 'http://localhost:8090/static//upload/video/course/2019/04/09/video_BiFhbLf.mp4',
  taskVideoTitle: ''
}

const getters = {

}

const mutations = {
  changeVideoSrc (state, taskVideoSrc) {
    state.taskVideoSrc = taskVideoSrc
  },
  changeVideoTitle (state, taskVideoTitle) {
    state.taskVideoTitle = taskVideoTitle
  }
}

const store = new Vuex.Store({
  state,
  getters,
  mutations
})

export default store
