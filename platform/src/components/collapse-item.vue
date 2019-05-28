<template>
  <div class="">
    <div class="content" @click="clickHandler()">
      <div class="chapter-name">
        <p class="fname">{{ item.title }}</p>
        <span class="rowdown" v-show="rowdown" v-if="item.sections.length > 0"></span>
        <span class="rowup" v-show="rowup" v-if="item.sections.length > 0"></span>
      </div>
      <div class="subchapter" v-show="isSubchapter" v-for="(sub, subid) in item.sections" :key="subid">
        <p class="subname">{{ sub.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 通过v-show控制显示，down三角朝下，up三角朝上，isSubchapter显示二级菜单
      rowdown: true,
      rowup: false,
      isSubchapter: false
    }
  },
  // 接收父组件（category大纲调用）传过来的值
  props: ['item', 'indexs'],
  methods: {
    clickHandler () {
      this.rowdown = !this.rowdown
      this.rowup = !this.rowup
      this.isSubchapter = !this.isSubchapter
    }
  }
}
</script>

<style lang="less" scoped>
.content{
  margin: 0 20px 50px;
  border: 1px solid #3976f1;
  cursor: pointer;
  .chapter-name{
    font-size: 17px;
    color: @font-white;
    padding-left: 2%;
    height: 50px;
    line-height: 50px;
    // 章前边小圆点样式
    &:before{
      content: '';
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #3976f1;
      position: relative;
      display: inline-block;
      margin-right: 4%;
    }
    .fname{
      display: inline-block;
    }
    .rowdown{
      width: 0;
      height: 0;
      border-top: 20px solid #3976f1;
      border-right: 10px solid transparent;
      border-left: 10px solid transparent;
      position: relative;
      display: block;
      top: 19px;
      right: 2%;
      float: right;
    }
    .rowup{
      display: none;
      width: 0;
      height: 0;
      border-bottom: 20px solid #3976f1;
      border-right: 10px solid transparent;
      border-left: 10px solid transparent;
      position: relative;
      display: block;
      top: 19px;
      right: 2%;
      float: right;
    }
  }
  .programname{
    &:before{
      background: #f29305;
    }
  }
  .subchapter{
    border-top: 1px solid #3976f1;
    height: 40px;
    line-height: 40px;
    width: 100%;
    .subname{
      padding-left: 8%;
      color: @font-white;
    }
  }
}
</style>
