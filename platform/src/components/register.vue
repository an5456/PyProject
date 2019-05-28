<template>
  <div class="login">
    <div class="loginbox">
      <ul class="login-tab">
        <li :class="showLogin ? 'active' : ''" @click="toLogin">登陆</li>
        <li :class="showRegister ? 'active' : ''" @click="toRegister">注册</li>
      </ul>
      <div class="reg-form" v-show="showRegister">
        <div class="reg-form2" v-show="showRegPassword">
          <div class="form-label">设置密码</div>
          <div class="form-input">
            <input type="password" v-model="password" />
          </div>
          <div class="form-label">重复密码</div>
          <div class="form-input">
            <input type="password" v-model="repassword"/>
          </div>
          <p class="errtext">{{ errorText }}</p>
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
      showLogin: false,
      showRegister: true,
      showRegPassword: true,
      password: '',
      repassword: '',
      errorText: ''
    }
  },
  computed: {
    // 检查两次输入的密码是否一致
    passErrors () {
      let errorText, status
      if (!this.password) {
        status = false
        errorText = '请输入密码'
      } else {
        if (this.password === this.repassword) {
          status = true
          errorText = ''
        } else {
          status = false
          errorText = '两次输入的密码不一致'
        }
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
    // 点击注册
    register () {
      let email, token
      if (this.passErrors.status) {
        console.log(location.pathname)
        let params = window.location.href.split('?')[1].split('&')
        if (params.length > 0) {
          email = unescape(params[0].split('=')[1])
          token = unescape(params[1].split('=')[1])
          this.$axios.post('/api/user/register2/', {
            params: {
              password1: this.password,
              password2: this.repassword,
              email: email,
              token: token
            }
          }).then(res => {
            if (res.status === 200) {
              this.$message({
                message: '注册成功，请登录',
                showClose: true,
                center: true,
                type: 'success'
              })
              this.$router.push({path: '/login'})
            }
          }).catch(err => {
            console.log('注册失败', err)
          })
        } else {
          console.log('返回邮箱token失败')
        }
      } else {
        this.errorText = this.passErrors.errorText
      }
    }
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
