<template>
  <div id="app">
    <v-header ref="child" @account="getAccount"></v-header>
    <router-view :account="account"/>
  </div>
</template>

<script>
import MarketPlace from '@/components/MarketPlace'
import Header from '@/components/Header'

export default {
  name: 'App',
  components:{
    MarketPlace,
    Header,
    'v-header':Header
  },
  data() {
    return{
      account: ''
    }
  },
  methods:{
    getAccount(msg) {
      this.account = msg;
      console.log(this.account);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif, Poppins;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
html, body, #app {
  height: 100%;
}
</style>
