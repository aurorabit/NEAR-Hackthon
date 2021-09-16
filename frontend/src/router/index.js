import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MarketPlace from '@/components/MarketPlace'
import Header from '@/components/Header'
import Creation from '@/components/Creation'
import Detail from '@/components/Detail'
import NFTOwner from '@/components/NFTOwner'
import NFTPawnBroker from '@/components/NFTPawnBroker'
import MyPawn from '@/components/MyPawn'
import Mine from '@/components/Mine'

const originalPush = Router.prototype.push;

Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MarketPlace',
      component: MarketPlace
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail
    },
    {
      path: '/market',
      name: 'MarketPlace',
      component: MarketPlace
    },
    {
      path: '/creation',
      name: 'Creation',
      component: Creation
    },
    {
      path: '/header',
      name: 'Header',
      component: Header
    },
    {
      path: '/nftowner',
      name: 'NFTOwner',
      component: NFTOwner
    },
    {
      path: '/pawnbroker',
      name: 'NFTPawnBroker',
      component: NFTPawnBroker
    },
    {
      path: '/mypawn',
      name: 'MyPawn',
      component: MyPawn
    },
    {
      path: '/mine/:',
      name: 'Mine',
      component: Mine
    },
    {
      path: '/mine/',
      name: 'Mine',
      component: Mine
    },
  ]
})
