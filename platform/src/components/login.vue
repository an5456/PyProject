<template>
  <div class="login">
    <div class="loginbox">
      <ul class="login-tab">
        <li :class="showLogin ? 'active' : ''" @click="toLogin">登陆</li>
        <li :class="showRegister ? 'active' : ''" @click="toRegister">注册</li>
      </ul>
      <div class="log-form" v-show="showLogin">
        <div class="form-label">邮箱</div>
        <div class="form-input">
          <input type="text" v-model="loginEmail"/>
        </div>
        <div class="form-label">密码</div>
        <div class="form-input">
          <input type="password" v-model="password" />
        </div>
        <div>
          <input type="checkbox" />
          <span>7天内自动登陆</span>
        </div>
        <p class="errtext">{{ errorText }}</p>
        <button class="btn" @click="login">立即登陆</button>
        <div class="lg-bottom">
          <a class="find">找回密码</a>
          <span class="line">|</span>
          <span class="content">还没有注册账号？</span>
          <a class="reg" @click="toRegister">立即注册</a>
        </div>
      </div>
      <div class="reg-form" v-show="showRegister">
        <div class="reg-form1" v-show="showRegFirst">
          <div class="form-label">输入您的邮箱</div>
          <div class="form-input">
            <input type="text" v-model="loginEmail" />
          </div>
          <p class="errtext">{{ errorText }}</p>
          <button class="btn" @click="toVertifyReg">立即注册</button>
          <div class="lg-bottom reg-bottom">
            <p class="content">注册即表示同意隐私策略和服务条款</p>
            <div class="tologin">已有账号？
              <a class="login" @click="toLogin">登陆</a>
            </div>
          </div>
        </div>
        <div class="reg-form2" v-show="showRegPassword">
          <div class="form-label">设置密码</div>
          <div class="form-input">
            <input type="text" v-model="password" />
          </div>
          <div class="form-label">重复密码</div>
          <div class="form-input">
            <input type="text" v-model="repassword"/>
          </div>
          <button class="btn" @click="register">完成注册</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      mystudy: '我的学习',
      showLogin: true,
      showRegister: false,
      showRegFirst: true,
      showRegPassword: false,
      loginEmail: '',
      password: '',
      repassword: '',
      errorText: ''
    }
  },
  computed: {
    // 检查用户输入的邮箱是否合法
    emailErrors () {
      let errorText, status
      if (!/@/g.test(this.loginEmail)) {
        status = false
        errorText = '邮箱格式不正确'
      } else {
        status = true
        errorText = ''
      }
      return {
        status,
        errorText
      }
    }
  },
  methods: {
    // 去登陆页面
    toLogin () {
      this.showLogin = true
      this.showRegister = false
    },
    // 跳转到注册页面
    toRegister () {
      this.showRegister = true
      this.showLogin = false
      this.showRegFirst = true
      this.showRegPassword = false
    },
    // 点击注册之后邮箱验证-》设置密码
    toVertifyReg () {
      let register2url = 'http://localhost:8080/#/register'
      if (!this.emailErrors.status) {
        this.errorText = this.emailErrors.errorText
      } else {
        this.$axios.post('/api/user/register1', {
          params: {
            email: this.loginEmail,
            register2url: register2url
          }
        }).then(res => {
          this.$message({
            message: '请前往邮箱查看',
            showClose: true,
            center: true,
            type: 'success'
          })
        }).catch(err => {
          console.log('邮箱数据异常', err)
        })
      }
    },
    // 点击注册
    register () {
      this.showRegister = false
      this.showLogin = true
    },
    // 点击登陆
    login () {
      this.$axios.post('api/user/login', {
        params: {
          username: this.loginEmail,
          password: this.password
        }
      }).then(res => {
        if (res.data.code === 2000) {
          // 把登录信息存储到session中
          sessionStorage.mystudy = this.mystudy
          sessionStorage.useremail = this.loginEmail
          sessionStorage.userId = res.data.userid
          this.$router.push({path: '/'})
        }
        if (res.data.code === 2001) {
          this.errorText = '用户名密码不正确'
        }
      }).catch(err => {
        console.log('登陆失败', err)
      })
    }
  },
  // 与请求后台接口
  created () {

  }
}
</script>

<style lang="less">
.plate-content{
  background: #f4fbff;
}
.login{
  background: #f4fbff;
  width: 100%;
}
.loginbox{
  width: 450px;
  height: 450px;
  background: #fff;
  border-radius: 4px;
  margin: auto;
  margin-top: 4%;
}
.errtext{
  color: @red;
  font-size: 14px;
}
.login-tab{
  padding: 30px 40px;
  li{
    display: inline-block;
    font-size: 16px;
    color: #212121;
    letter-spacing: 3px;
    padding-right: 40px;
    cursor: pointer;
  }
  .active{
    color: #567fe3;
    font-weight: bold;
    text-decoration: underline #567fe3;
  }
}
.log-form,.reg-form{
  padding: 10px 40px 0;
}
.form-label{
  font-size: 14px;
  color: #717171;
  padding-bottom: 10px;
}
.form-input{
  padding-bottom: 20px;
  input{
    width: 370px;
    height: 40px;
    border-radius: 2px;
    background: #f2f2f2;
    border: none;
  }
}
.btn{
  width: 370px;
  height: 40px;
  line-height: 40px;
  background-color: #567fe3;
  border-radius: 2px;
  color: #fff;
  letter-spacing: 3px;
  border: none;
  font-size: 14px;
  margin-top: 40px;
}
.lg-bottom{
  font-size: 14px;
  margin-top: 15px;
  letter-spacing: 2px;
  a{
    color: #567fe3;
    cursor: pointer;
  }
  .content{
    color: #717171;
  }
  .reg{
    display: inline-block;
    float: right;
  }
}
.reg-bottom{
  .content{
    text-align: center;
  }
  .tologin{
    text-align: center;
    padding-top: 20px;
  }
}
</style>
