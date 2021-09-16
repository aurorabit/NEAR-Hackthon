<template>
  <div id="mostheader" style="background:#FFF;color:#000;margin-top:0px;width:100%">
    <div
        style="vertical-align:middle; left:0px; right:0px; height:5%;width:100%;border-width: 0px 0px 2px 0px;border-style:solid;border-color: #E3E1E3">
      <el-row style="vertical-align:middle;">
        <!-- <el-menu  mode="horizontal"  style="background:#FFF;color:#000;height:120px"> -->
        <el-col :span="1" style="margin-left:6.6%;width:3.06%;margin-top:1.02%">
          <div style="text-align:center;height:100%;vertical-align:middle;">
            <router-link to="/">
              <img src="../assets/logo.svg" style="vertical-align:middle;">
            </router-link>
          </div>
        </el-col>

        <el-col :span="1" style="width:43.63%;margin-top:1.36%;margin-left:1.4%;">
          <div style="vertical-align:middle;text-align:center;height:2%">
            <el-input class="searchInput" placeholder="Search items here" prefix-icon="iconfont el-icon-search"
                      v-model="search_input"></el-input>
          </div>
        </el-col>


        <el-col :span="1" style="margin-left:7.52%;margin-top:1.7%;width:12.1%;">
          <div style="vertical-align:middle;text-align:center;">
            <router-link to="/market">
              <div class="marketplace">Marketplace</div>
            </router-link>
          </div>
        </el-col>

        <el-col :span="1" style="margin-left:0.77%;margin-top:1.34%;width:7.6%">
          <div style="vertical-align:middle;text-align:center;">
            <router-link to="/creation">
              <el-button class="createBtn">
                <div class="create_font">Create</div>
              </el-button>
            </router-link>
          </div>
        </el-col>

        <el-col :span="1" style="vertical-align:middle;margin-left:0.7%;margin-top:1.34%;width:10.16%">
          <div style="vertical-align:middle;text-align:center;width:100%;">
            <el-button v-if="account==''" class="connectBtn" v-on:click="connnectWallet">
              <div class="connect_font">Connect</div>
            </el-button>
            <div v-else class="connect_after">
              <div class="connect_font">
                <el-row>
                  <el-col :span="12" style="text-align:left">
                    <el-image style="border-radius:100%;"
                              :style="'height:'+myHeight * 0.05 +'px;width:'+myHeight * 0.05 +'px;'"
                              :src="head_url">
                    </el-image>
                  </el-col>
                  <el-col :span="12">
                    {{ accountShort }}
                  </el-col>
                </el-row>
              </div>
            </div>
          </div>
        </el-col>

        <el-col :span="1" style="margin-left:2.16%;margin-top:1.67%;width:4.3%">
          <div style="vertical-align:middle;text-align:center;">
            <el-dropdown>
              <div style="text-align:center;height:100%;vertical-align:middle;">
                <!-- <router-link to="/mine"> -->
                <img src="../assets/mine_icon.svg" @click="viewMine" width="24px" height="24px"
                     style="vertical-align:middle;cursor:pointer">
                <!-- </router-link> -->
              </div>
              <el-dropdown-menu slot="dropdown">
                <router-link :to="{path:'/mine',query: {id: '1'}}">
                  <el-dropdown-item>NFT</el-dropdown-item>
                </router-link>
                <router-link :to="{path:'/mine',query: {id: '2'}}">
                  <el-dropdown-item>PawnBroker</el-dropdown-item>
                </router-link>
                <router-link :to="{path:'/mine',query: {id: '3'}}">
                  <el-dropdown-item>Pawn</el-dropdown-item>
                </router-link>
                <el-dropdown-item @click.native="logOut">Log Out</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </el-col>
        <div class="menu_line">

        </div>
      </el-row>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      myHeight: document.documentElement.clientWidth * 0.3,
      searchVisible: true,
      input2: '',
      idenisadmin: false,
      search_input: '',
      account: '',
      accountShort: '',
      head_url: require("../assets/user_head.png"),
    }
  },

  methods: {
    logOut() {
      this.account = '';
      this.setAccount();
      this.accountShort = '';
    },
    viewMine() {
      if (this.account == undefined || this.account == '') {
        this.$message.error("Please Connect Your Wallet!");
        return;
      } else
        this.$router.push({
          path: '/mine',
          query: Object.assign({}, this.$route.query, {_: +new Date()})
        });
    },

    //检索
    search() {
      console.log("检索:" + this.search_input);
    },
    async connnectWallet() {
      console.log("try to connect wallet");

      let account = await window.ethereum.send('eth_requestAccounts')
      console.log(account.result[0])
      this.account = account.result[0]
      this.setAccount();
      this.accountShort = this.account.substr(0, 5) + '...' + this.account.substr(this.account.length - 5);


      return;


      // let accounts = await ethereum.send("cfx_requestAccounts");
      //  this.account = accounts[0];
      // console.log(this.account);
      // this.setAccount();
      // this.accountShort = this.account.substr(0, 5) + '...' + this.account.substr(this.account.length - 5);
    },
    setAccount() {
      this.$emit('account', this.account);
    }
  }

}

</script>

<style scoped>
.grid-content {
  min-height: 16px;
}

a {
  text-decoration: none
}

a:hover {
  text-decoration: none
}

.marketplace {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  display: flex;
  align-items: center;

  /* Black/1 */

  color: #2D2E36;


  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 0px 20px;
}

.router-link-active {
  text-decoration: none;
}

.el-input__inner {
  border-color: #E3E1E3;
}

.createBtn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 9px 30px;

  /* position: absolute; */
  width: 109px;
  height: 40px;
  /* left: 984px;
  top: 6.5px; */

  /* Dark */

  background: #24252D;
  border: 1px solid #000000;
  box-sizing: border-box;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.create_font {
  position: static;
  width: 49px;
  height: 23px;
  /* left: 30px;
  top: 8.5px; */

  /* Button */

  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;

  /* White */

  color: #FFFFFF;


  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 10px;
}

.connectBtn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 9px 30px;

  /* position: absolute; */
  width: 146px;
  height: 40px;
  /* left: 1103px;
  top: 6.5px; */

  /* Dark */
  background: #FFF;
  border: 1px solid #24252D;
  box-sizing: border-box;
  border-radius: 10px;
}

.connect_after {
  display: flex;
  flex-direction: row;
  /* justify-content: center; */
  align-items: center;
  text-align: center;
  vertical-align: middle;
  /* padding: 9px 30px; */

  /* position: absolute; */
  width: 146px;
  height: 40px;
  /* left: 1103px;
  top: 6.5px; */

  /* Dark */
  background: #FFF;
  border: 1px solid #24252D;
  box-sizing: border-box;
  border-radius: 10px;

  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border: 1px solid #E3E1E3;
  box-sizing: border-box;
  border-radius: 10px;
}

.connect_font {
  position: static;
  width: 62px;
  height: 23px;
  /* left: 42px;
  top: 9px; */

  /* Button */

  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;

  /* Dark */

  color: #24252D;


  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 10px;
}

.menu_line {
  position: static;
  /* width: 99.9%; */
  height: 0px;
  /* left: -5.5px;
  top: 65.5px; */

  /* Grey/Gray/1 */

  /* border: 1px solid #E3E1E3; */

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 30px 0px;
  margin-top: 5.02%
}

.searchInput >>> .el-input__inner:focus {
  border-color: #000;
}

</style>
