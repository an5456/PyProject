<template>
  <div class="aside-main-width">
    <div class="info">
      <el-form ref="form" :model="form" label-width="80px">
        <div class="item">
          <div class="info-img">
            <img class="center-block" src="../../../assets/images/info/name.png" />
          </div>
          <el-form-item label="用户昵称">
            <el-input v-model="form.nicname"></el-input>
          </el-form-item>
        </div>
        <div class="item">
          <div class="info-img">
            <img class="center-block" src="../../../assets/images/info/pass.png" />
          </div>
          <el-form-item label="登陆密码" prop="pass">
            <el-input type="password" v-model="form.pass" autocomplete="off"></el-input>
            <span class="info">有助于保护您的账号安全</span>
          </el-form-item>
        </div>
        <div class="item">
          <div class="info-img">
            <img class="center-block" src="../../../assets/images/info/email.png" />
          </div>
          <el-form-item label="绑定邮箱">
            <el-input v-model="form.email"></el-input>
            <span class="info">方便第一时间为您服务</span>
          </el-form-item>
        </div>
        <div class="item">
          <div class="info-img">
            <img class="center-block" src="../../../assets/images/info/payapss.png" />
          </div>
          <el-form-item label="支付密码">
            <el-input type="password" v-model="form.payPassword"></el-input>
            <span class="info">用于保护您的支付安全</span>
          </el-form-item>
        </div>
        <div class="item">
          <div class="info-img">
            <img class="center-block" src="../../../assets/images/info/tel.png" />
          </div>
          <el-form-item label="手机绑定">
            <el-input v-model="form.tel"></el-input>
            <span class="info">增强登录、支付时的安全性，同时也可以用于找回密码和支付密码</span>
          </el-form-item>
        </div>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">保存</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        nicname: '',
        pass: '',
        email: '',
        payPassword: '',
        tel: ''
      },
      userEmail: sessionStorage.useremail
    }
  },
  created () {
    this.$axios.post('/api/user/getuserinfo', {
      params: {
        userid: sessionStorage.userId
      }
    }).then(res => {
      if (res.data.email !== null || res.data.email !== '') {
        this.form.email = res.data.email
      }
      if (res.data.nickname !== null || res.data.nickname !== '') {
        this.form.nicname = res.data.nickname
      }
      if (res.data.password !== null || res.data.password !== '') {
        this.form.pass = res.data.password
      }
      if (res.data.paypassword !== null || res.data.paypassword !== '') {
        this.form.payPassword = res.data.paypassword
      }
      if (res.data.telphone !== null || res.data.telphone !== '') {
        this.form.tel = res.data.telphone
      }
    }).catch(err => {
      console.log('获取用户信息失败' + err)
    })
  },
  methods: {
    onSubmit () {
      this.$axios.post('/api/user/setuserinfo', {
        params: {
          userid: sessionStorage.userId,
          nickname: this.form.nicname,
          password: this.form.pass,
          email: this.form.email,
          paypassword: this.form.payPassword,
          telphone: this.form.tel
        }
      }).then(res => {
        console.log(res)
      }).catch(err => {
        console.log('修改信息失败' + err)
      })
    }
  }
}
</script>

<style lang="less" scoped>
.info{
  padding-top: 3.3975rem;
  padding-left: 1.875rem;
  padding-bottom: 15rem;
  .el-form{
    .item{
      .info-img{
        display: inline-block;
        position: relative;
        top: 3px;
        width: 20px;
      }
      .el-form-item{
        display: inline-block;
        .el-form-item__label{
          color: @gray;
        }
        .el-input{
          width: 14.0625rem;
          height: 1.34rem;
        }
        .info{
          font-size: 12px;
          color: @gray-mid;
        }
        .el-button{
          width: 9.375rem;
          background: @blue;
          border-color: @blue;
          margin-left: 5%;
          margin-top: 10.78125rem;
        }
      }
    }

  }
}
</style>
