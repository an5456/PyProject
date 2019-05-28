<template>
  <div class="circle">
    <canvas :id="id" width="300" height="300" style="width:150px;height:150px;"></canvas>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data () {
    return {
      num: 0,
      canvas: '',
      context: '',
      cirX: '',
      cirY: '',
      rad: '',
      n: 1,
      r: 60,
      // id用来标识有几个圆环，当有并排好几个圆环的时候，可以从父页面把值传过来
      id: '1'
    }
  },
  props: ['percent'],
  mounted () {
    this.canvas = document.getElementById(this.id)
    this.context = this.canvas.getContext('2d')
    this.context.scale(2, 2)
    this.cirX = 75 // this.canvas.width/ 2
    this.cirY = 75 // this.canvas.height/ 2
    this.rad = Math.PI * 2 / 100
    this.DreamLoading()
  },
  methods: {
    // 绘制最外层细圈
    writeCircle () {
      this.context.save() // save和restore可以保证样式属性只运用于该段canvas元素
      this.context.beginPath() // 开始路径
      this.context.strokeStyle = '#EEF0F5' // 设置边线的颜色
      this.context.lineWidth = 10
      this.context.arc(this.cirX, this.cirY, this.r, 0, Math.PI * 2, false) // 画一个圆的路径
      this.context.stroke() // 绘制边线
      this.context.closePath()
    },
    // 绘制文本
    writeText (n) {
      this.context.save()
      this.context.font = '14px Arial'
      this.context.fillStyle = '#9a9a9a' // 字体颜色
      this.context.fillText('学习进度', this.cirX - 30, this.cirY - 10) // 绘制实心
      this.context.font = '20px Arial'
      this.context.fillStyle = '#567fe3' // 字体颜色
      this.context.fillText(n.toFixed(0) + '%', this.cirX - 20, this.cirY + 20) // 绘制实心
      this.context.stroke()
      this.context.restore()
    },
    // 绘制蓝色外圈
    writeBlue (n) {
      this.context.save()
      this.context.strokeStyle = '#567fe3'
      this.context.lineWidth = 10
      this.context.lineCap = 'round'
      this.context.beginPath()
      this.context.arc(this.cirX, this.cirY, this.r, -Math.PI / 2, -Math.PI / 2 + this.rad * n, false)
      this.context.stroke()
      this.context.restore()
    },
    DreamLoading () {
      // 清除所有，重新绘制
      this.context.clearRect(0, 0, this.canvas.width, this.canvas.height)
      this.writeCircle()
      this.writeText(this.n)
      this.writeBlue(this.n)
      if (this.n <= this.percent) {
        this.n = this.n + 0.4
      } else {
        return this.n = 0
      }
      requestAnimationFrame(this.DreamLoading)
    }
  }
}
</script>

<style lang="less" scoped>

</style>
