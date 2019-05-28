<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="less">
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
  display: block;
}
body {
  line-height: 1;
}
ol, ul {
  list-style: none;
}
blockquote, q {
  quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
  content: '';
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
a {
  color: inherit;
  text-decoration: none;
}

html,body{
  height: 100%;
}
body {
  background: #ffffff;
  font-family: "Helvetica Neue",Helvetica,Arial,"Hiragino Sans GB","Hiragino Sans GB W3","Microsoft YaHei UI","Microsoft YaHei","WenQuanYi Micro Hei",sans-serif;
  font-size: 16px;
  color: #444;
}
#app{
  height: 100%;
}
.plate-main{
  // width: 1120px;
  // margin: auto;
  display: flex;
  flex-direction: column;
  height: 100%;
}
.plate-header{
  width: 100%;
  height: 60px;
  background: #ffffff;
  box-shadow: 2px 2px 2px rgba(220,236,251,.7);
  .header-inner{
    width: 100%;
    .logo{
      float: left;
      width: calc(50% - 560px);
      height: inherit;
      img{
        width: 100px;
        height: 50px;
        margin: auto;
      }
    }
    .header-nav{
      width: 1120px;
      height: inherit;
      line-height: 60px;
      float: left;
      ul{
        li{
          display: inline-block;
        }
      }
    }
    .header-right{
      float: left;
      width: calc(50% - 560px);
      height: inherit;
      line-height: 60px;
      ul{
        li{
          display: inline-block;
        }
      }
    }
  }
}
.plate-content{
  width: 100%;
  background: blueviolet;
  flex-grow: 1;
  .contain{
    width: 1120px;
    margin: auto;
    background: yellow;
  }
}
.plate-footer{
  width: 100%;
  height: 60px;
  background: grey;
}
</style>
