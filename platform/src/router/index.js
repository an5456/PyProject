import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import Layout from '@/components/layout'
import IndexPage from '@/pages/index'
import Login from '@/components/login'
import Register from '@/components/register'

import InfoMachineLearning from '@/pages/course-introduce/mechine-learning'

import Order from '@/pages/order/order'

import My from '@/pages/my/index'
import MyInfo from '@/pages/my/info/myinfo'
import Study from '@/pages/my/study/study'
import Test from '@/pages/my/test/test'
import Test1 from '@/pages/my/test/test1'

import myCourse from '@/pages/my/course/course'
import myTask from '@/pages/my/course/task'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'IndexPage',
      component: IndexPage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/info-machine-learning',
      name: 'InfoMachineLearning',
      component: InfoMachineLearning
    },
    {
      path: '/order',
      name: 'Order',
      component: Order
    },
    {
      path: '/my',
      name: 'My',
      component: My,
      redirect: '/my/study',
      children: [
        {
          path: 'myinfo',
          name: 'MyInfo',
          component: MyInfo
        },
        {
          path: 'study',
          name: 'Study',
          component: Study
        },
        {
          path: 'test',
          name: 'Test',
          component: Test,
          redirect: '/test/test1',
          children: [
            {
              path: 'test1',
              name: 'Test1',
              component: Test1
            }
          ]
        }
      ]
    },
    {
      path: '/mycourse',
      name: 'myCourse',
      component: myCourse
    },
    {
      path: '/mytask',
      name: 'myTask',
      component: myTask
    }
  ]
})
