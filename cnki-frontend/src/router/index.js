import Vue from 'vue'
import Router from 'vue-router'
import index from '@/layouts/index'
import hotAnalyse from '@/layouts/hotAnalyse'
import onlineSpider from '@/layouts/onlineSpider'
import chartAnalyse from '@/layouts/chartAnalyse'
import paperDetail from '@/layouts/paperDetail'
import store from '@/store/index.js'
const originalPush = Router.prototype.push
Router.prototype.push = function push(location, onResolve, onReject) {
  if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject)
  return originalPush.call(this, location).catch(err => err)
}
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/hotAnalyse',
      name: 'hotAnalyse',
      component: hotAnalyse
    },
    {
      path: '/onlineSpider',
      name: 'onlineSpider',
      component: onlineSpider,
      meta: {
        requireLogin: true // 添加该字段，表示进入这个路由是需要登录的
      },
    },
    {
      path: '/chartAnalyse',
      name: 'chartAnalyse',
      component: chartAnalyse,
      meta: {
        requireLogin: true // 添加该字段，表示进入这个路由是需要登录的
      },
    },
    {
      path: '/keywordAnalyse',
      name: 'keywordAnalyse',
      component: () => import("@/layouts/keywordAnalyse"),
      meta: {
        requireLogin: true // 添加该字段，表示进入这个路由是需要登录的
      },
    },
    {
      path: '/paperDetail',
      name: 'paperDetail',
      component: paperDetail,
      meta: {
        requireLogin: true // 添加该字段，表示进入这个路由是需要登录的
      },
    },
    {
      path: "/login",
      name: 'login',
      component: () => import("@/views/login")
    },
    {
      path: "/register",
      name: 'register',
      component: () => import("@/views/register")
    }
  ]
})

// 设置路由拦截
// 在vue-router的全局钩子中设置拦截 
// 每个路由皆会的钩子函数
// to 进入 from 离开 next 传递
// 不考虑刷新浏览器的情况，
// 实现了在各个需要登录和不需要登录状态之间跳转的拦截
// 底部是另外两个拦截条件不同的路由拦截方案，仅记录当时的思考

router.beforeEach((to, from, next) => {
  if (to.meta.requireLogin) {
    // 通过判断状态中是否存在user.name
    // 浏览store中的代码即可了解
    // 此次实例简化了state，只将流程跑通
    // !! 但是只通过vuex维护的全局状态中是否含有user信息
    // 当浏览器刷新时，所有状态将被清空，每次都会被重定向至登录页，
    // 因此有了http拦截的意义，底部有解释
    // console.log(store.state.user)
    // console.log(store.state)
    console.log(localStorage.getItem('name'), 'store.state.name')
    if (localStorage.getItem('name')) {
      next();
    } else {
      // next({path:xxx})当前的导航被中断，然后进行一个新的导航
      next({
        path: '/login',
        // $router.path 
        // 一个 key/value 对象，表示 URL 查询参数。
        // 例如，对于路径 /foo?user=1，则有 $route.query.user == 1，
        // 如果没有查询参数，则是个空对象。
        // 假设一开始进入 / (首页)并且没有登录 ，则next进行跳转的路由为/login 
        // 之后登录成功 则redirect => to.fullPath（即为开始进入的路由） => / (首页)
        query: {
          redirect: to.fullPath
        }
        // 将跳转的路由path作为参数，登录成功后跳转到该路由
        // $router.fullPath 完成解析后的 URL，包含查询参数和 hash 的完整路径
      })
    }
  } else {
    next();
  }
})

export default router;