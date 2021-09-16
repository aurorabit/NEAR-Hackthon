<template>
  <div>
    <div>
      <el-image style="width: 100%;  top: 0%" :src="title_bg"></el-image>
    </div>

    <div style="margin-top:-6.35%">
      <el-image class="head_pic" :src="title_head"></el-image>
      <div class="account_name">
        {{ account }}
      </div>
    </div>


    <el-row style="width:80%;margin-left:10%;">
      <el-col :span="18" style="width:65%;margin-top:1.36%;margin-left:1.4%;text-align:left">
        <div class="searchDiv">
          <el-input class="searchInput" placeholder="Search items here" prefix-icon="iconfont el-icon-search"
                    v-model="search_input"></el-input>
        </div>
      </el-col>
      <el-col :span="6" style="width:21%;margin-top:1.36%;text-align:right">
        <el-select v-model="value" placeholder="Please choose" @change="changeTab">
          <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>

    <div v-for="item in my_nft" :key="item.id" v-show="showMyNft">
      <el-row style="margin-top:1.4%">
        <el-col :span="4" style="margin-left:11%;height:15.19%;width:16.21%">
          <router-link :to="{path:'/nftowner',query: {id: item.id[0], uri: item.uri[0]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[0]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[0] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[1] !== undefined">
          <router-link :to="{path:'/nftowner',query: {id: item.id[1], uri: item.uri[1]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[1]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[1] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[2] !== undefined">
          <router-link :to="{path:'/nftowner',query: {id: item.id[2], uri: item.uri[2]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[2]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[2] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[3] !== undefined">
          <router-link :to="{path:'/nftowner',query: {id: item.id[3], uri: item.uri[3]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[3]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[3] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>

      </el-row>

    </div>

    <div v-for="item in pawn_broker" :key="item.id" v-show="showPawnBroker">
      <el-row style="margin-top:1.4%">
        <el-col :span="4" style="margin-left:11%;height:15.19%;width:16.21%">
          <router-link :to="{path:'/pawnbroker',query: {id: item.id[0], uri: item.uri[0]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[0]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[0] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[1] !== undefined">
          <router-link :to="{path:'/pawnbroker',query: {id: item.id[1], uri: item.uri[1]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[1]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[1] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[2] !== undefined">
          <router-link :to="{path:'/pawnbroker',query: {id: item.id[2], uri: item.uri[2]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[2]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[2] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[3] !== undefined">
          <router-link :to="{path:'/pawnbroker',query: {id: item.id[3], uri: item.uri[3]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[3]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[3] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>

      </el-row>

    </div>

    <div v-for="item in my_pawn" :key="item.id" v-show="showMyPawn">
      <el-row style="margin-top:1.4%">
        <el-col :span="4" style="margin-left:11%;height:15.19%;width:16.21%">
          <router-link :to="{path:'/mypawn',query: {id: item.id[0], uri: item.uri[0]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[0]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[0] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[1] !== undefined">
          <router-link :to="{path:'/mypawn',query: {id: item.id[1], uri: item.uri[1]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[1]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[1] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[2] !== undefined">
          <router-link :to="{path:'/mypawn',query: {id: item.id[2], uri: item.uri[2]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[2]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[2] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>
        <el-col :span="4" style="margin-left:1.39%;width:16.21%" v-if="item.id[3] !== undefined">
          <router-link :to="{path:'/mypawn',query: {id: item.id[3], uri: item.uri[3]}}">
            <el-card style="border-radius:20px;">
              <el-image style=" border-radius:30px;"
                        :style="'height:'+myHeight+'px;width:'+myWidth+'px;'"
                        :src="item.url[3]"
                        :fit='cover'
              >
              </el-image>
              <div style="text-align:left;margin-top:10px">
                <b style="font-size:16px">{{ item.name[3] }}</b>
              </div>
            </el-card>
          </router-link>
        </el-col>

      </el-row>

    </div>

  </div>

</template>


<script>
import Vue from 'vue'
import Header from '@/components/Header'
import {ethers} from "ethers";
import {MathArtAddress, NFiTMarketAddress} from "../../sol/config.json";
import {abi} from "../../sol/NFiTMarket.json";

Vue.component('profile-box', {
  props: ['title', 'address', 'icon'],
  template: '<div><el-col><el-images style="width: 100px; height: 100px" :src="url"></el-images></el-col><el-col><el-row>{{ title }}</el-row><el-row>{{ address }}</el-row></el-col></div>'
});

export default {
  props: ['account'],
  data() {
    return {
      myWidth: document.documentElement.clientWidth * 0.14,
      myHeight: document.documentElement.clientHeight * 0.25,
      options: [{
        value: '1',
        label: 'My NFTs'
      }, {
        value: '2',
        label: 'Pawn Broker'
      }, {
        value: '3',
        label: 'My Pawn'
      },],
      value: '1',
      search_input: '',
      activeName: 'first',
      url: 'https://d3vi7ke2kcvale.cloudfront.net/images/bsc/0xe3748766528f93887503dbb527f0965614d72e61/f4b6ceef17ba9360d61d2d1fb40a04c2.png',
      title_bg: require("../assets/mine_bg.png"),
      title_head: require("../assets/mine_head.png"),
      nft_info: {
        name: 'demo NFT',
        date: '2020-10-10',
        theme: 'Future',
        style: 'Fiction',
        number: 1,
        serial: '',
        type: '',
        description: '组才能到课程建设你看金牛座存款证明······新耳机of扣款，出来的，出来的，V领大V，定律',
        royality: 10,
        url: '../../static/default.png',
        creator: '0x7b832869D5c27355484eA1490D3B90ea5951f828',
        owner: '0x3cC101325F4E644E43F8e4Fe389F160EfB4996d3',
      },
      url1: require("../assets/demoNFT_1.png"),
      url2: require("../assets/demoNFT_2.png"),
      url3: require("../assets/demoNFT_3.png"),
      url4: require("../assets/demoNFT_4.png"),
      url5: require("../assets/demoNFT_5.png"),
      url6: require("../assets/demoNFT_6.png"),
      url7: require("../assets/demoNFT_7.png"),
      url8: require("../assets/demoNFT_8.png"),
      sale_price: 0,
      loan_price: 0,
      creator_info: {
        nick_name: 'xhdcf',
        icon: '../../static/default-icon.png',
        description: 'EVOLUTION is a new collectible balabala, which I could find nothing with it but I think it is somehow interesting',
      },
      owner_info: {
        nick_name: 'alibaba',
        icon: '../../static/default-icon.png',
        description: 'EVOLUTION is a new collectible balabala, which I could find nothing with it but I think it is somehow interesting',
      },
      currentDate: '2021-08-12',
      my_nft: [
        {
          id: [0, 1, 2, 3],
          name: ['test', 'test2', 'test3', 'test4'],
          uri: ['', '', '', ''],
          url: [require("../assets/demoNFT_1.png"), require("../assets/demoNFT_2.png"), require("../assets/demoNFT_3.png"), require("../assets/demoNFT_4.png")]
        },
        {
          id: [0, 1, 2, 3],
          name: ['test', 'test2', 'test3', 'test4'],
          uri: ['', '', '', ''],
          url: [require("../assets/demoNFT_1.png"), require("../assets/demoNFT_2.png"), require("../assets/demoNFT_3.png"), require("../assets/demoNFT_4.png")]
        },
      ],
      pawn_broker: [
        {
          id: [0, 1, 2, 3],
          name: ['test', 'test2', 'test3', 'test4'],
          uri: ['', '', '', ''],
          url: [require("../assets/demoNFT_4.png"), require("../assets/demoNFT_5.png"), require("../assets/demoNFT_6.png"), require("../assets/demoNFT_7.png")]
        },
        {
          id: [0, 1, 2,],
          name: ['test', 'test2', 'test3', 'test4'],
          uri: ['', '', '', ''],
          url: [require("../assets/demoNFT_4.png"), require("../assets/demoNFT_5.png"), require("../assets/demoNFT_6.png"), require("../assets/demoNFT_7.png")]
        }
      ],
      my_pawn: [
        {
          id: [0, 1, 2, 3],
          name: ['test', 'test2', 'test3', 'test4'],
          uri: ['', '', '', ''],
          url: [require("../assets/demoNFT_4.png"), require("../assets/demoNFT_5.png"), require("../assets/demoNFT_6.png"), require("../assets/demoNFT_7.png")]
        },
        {
          id: [0, 1,],
          name: ['test', 'test2',],
          uri: ['', ''],
          url: [require("../assets/demoNFT_4.png"), require("../assets/demoNFT_5.png")]
        }
      ],
      showMyNft: false,
      showPawnBroker: false,
      showMyPawn: false,
      json_url: '',
    }
  },
  beforeRouteUpdate(to, from, next) {
    if (to.fullPath !== from.fullPath)
      this.update();
    next();
    // react to route changes...
    // don't forget to call next()
  },
  mounted() {
    // console.log(this.account);
    this.my_nft = [];
    this.pawn_broker = [];
    this.my_pawn = [];

    this.get_bodySize();
    this.update();
    let _this = this;

    const {ethers} = require("ethers");
    const {abi, bytecode} = require('../../sol/NFiTMarket.json');
    const {NFiTMarketAddress} = require('../../sol/config.json');

    const provider = new ethers.providers.Web3Provider(window.ethereum)
    const signer = provider.getSigner()

    async function main() {
      let account = _this.account;
      if (!account) {
        _this.$message.error("Please connect to wallet");
        return;
      }

      let contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
      console.log("contract");
      console.log(contract);

      // function getUserOwnedNFT(address user) external view returns (uint[] memory itemIdList)
      var userOwnedNFT = await contract.getUserOwnedNFT(account);


      console.log("userOwnedNFT");
      console.log(userOwnedNFT);
      await _this.fillNFTInfoBrief(userOwnedNFT, _this.my_nft);



      // function getUserPawnedNFT(address user) external view returns (uint[] memory itemIdList)
      var userPawnedNFT = await contract.getUserPawnedNFT(account);

      await _this.fillNFTInfoBrief(userPawnedNFT, _this.my_pawn);

      // function getUserReceivedNFT(address user) external view returns (uint[] memory itemIdList)
      var userReceivedNFT = await contract.getUserReceivedNFT(account);
      await _this.fillNFTInfoBrief(userReceivedNFT, _this.pawn_broker);
    }

    main().catch(e => console.error(e));
  },
  methods: {
    async fillNFTInfoBrief(nftInfos, target) {
      let _this = this;
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress} = require('../../sol/config.json');

      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()
      async function main() {
        let contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        console.log(contract);
        var nfts = [];
        let item = {
          ID: '', name: '', sell_price: '', loan_price: '', url: '', uri: ''
        };
        for (var i = 0; i < nftInfos.length; i++) {
          let nftId = nftInfos[i][0].toString();
          if (nftId === "0") continue;
          // if(nftId ==="1") continue;
          console.log(nftId);
          item = {
            ID: '', name: '', sell_price: '', loan_price: '', url: '', uri: ''
          };
          // console.log(userOwnedNFT[i]);
          let itemId = nftId;
          let itemInfo = nftInfos[i];// contract.getItemInfo(itemId);
          console.log(itemInfo);
          {
            console.log("具体的内容");
            console.log("第一项是itemId");
            console.log(itemInfo[0].toString());
            console.log("第二项是nftContract");
            console.log(itemInfo[1]);
            console.log("第三项是tokenId");
            console.log(itemInfo[2].toString());
            console.log("第四项是creator");
            console.log(itemInfo[3]);
            console.log('第五项是pawnor');
            console.log(itemInfo[4]);
            console.log('第六项是owner');
            console.log(itemInfo[5]);
            console.log('第七项目是sellPrice');
            console.log(itemInfo[6].toString());
            console.log('第八项是loanPrice')
            console.log(itemInfo[7].toString())
            console.log('第九项是redeemPrice')
            console.log(itemInfo[8].toString())
            console.log('第十项是royalty')
            console.log(itemInfo[9].toString())
            console.log('第十项是deadline')
            console.log(itemInfo[10].toString())
            console.log('第十一项是state')
            console.log(itemInfo[11].toString())

          }


          let tokenId = itemInfo[2].toString();

          await _this.getUrl(tokenId);
          let itemUrl = _this.json_url;
          item.uri = itemUrl;
          let url = _this.$url + 'download/' + itemUrl.substr(0, itemUrl.length - 5);

          item.ID = itemId;
          await _this.getName(itemUrl);
          item.name = _this.temp_name;
          item.url = url;

          nfts.push(item);

        }

        var temp_map = {id: [], name: [], sale_price: [], pawn_price: [], url: [], uri: []};
        var count = 0;

        for (let i = 0; i < nfts.length; i++) {
          temp_map['id'].push(nfts[i].ID);
          temp_map['name'].push(nfts[i].name);
          temp_map['url'].push(nfts[i].url);
          temp_map['uri'].push(nfts[i].uri);
          count++;
          if (count == 4) {
            _this.my_nft.push(temp_map);
            temp_map = {id: [], name: [], sale_price: [], pawn_price: [], url: [], uri: []};
            count = 0;
          }
        }
        if (temp_map['id'].length > 0)
          target.push(temp_map);
      }

      main().catch(e => console.error(e));
    },

    async getUrl(tokenId) {
      let _this = this;
      await this.getJsonUrl(tokenId);
    },


    async getJsonUrl(tokenId) {
      const { ethers } = require("ethers");
      const {abi, bytecode} = require('../../sol/MathArt.json');
      const {MathArtAddress} = require('../../sol/config.json');
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()

      let _this = this;

      const contract = new ethers.Contract(MathArtAddress, abi,signer);

      console.log(contract);
      var url = await contract.tokenURI(tokenId);
      // alert(url);
      _this.json_url = url;
    },
    async getName(itemUrl) {
      let _this = this;
      await this.$http.request({
        url: _this.$url + 'download/' + itemUrl,
        method: 'get',
      }).then(response => {
        var responseData = response.data;
        _this.temp_name = responseData.nft_name;
      }).catch(function (e) {
        console.log(e);
      });
    },
    get_bodySize() {//动态获取浏览器高度 宽度
      const _this = this;
      window.onresize = () => {
        return (() => {
          _this.clientHeight = document.documentElement.clientHeight;
          _this.myHeight = _this.clientHeight * 0.25;
          _this.clientWidth = document.documentElement.clientWidth;
          _this.myWidth = this.clientWidth * 0.14;
        })();
      };
    },
    create() {
      console.log("login");
    },
    update() {
      if (this.$route.query.id == '2') {
        this.showPawnBroker = true;
        this.showMyNft = false;
        this.showMyPawn = false;
        this.value = '2';
      } else if (this.$route.query.id == '3') {
        this.showPawnBroker = false;
        this.showMyNft = false;
        this.showMyPawn = true;
        this.value = '3';
      } else {
        this.showPawnBroker = false;
        this.showMyNft = true;
        this.showMyPawn = false;
        this.value = '1';
      }
      ;
    },
    changeTab() {
      // console.log(this.$route);
      if (this.value === '2') {
        this.showPawnBroker = true;
        this.showMyNft = false;
        this.showMyPawn = false;
        this.$route.query.id = '2';
        this.$router.push({
          path: this.$route.path,
          query: Object.assign({}, this.$route.query, {_: +new Date()})
        });
      } else if (this.value === '3') {
        this.showPawnBroker = false;
        this.showMyNft = false;
        this.showMyPawn = true;
        this.$route.query.id = '3';
        this.$router.push({
          path: this.$route.path,
          query: Object.assign({}, this.$route.query, {_: +new Date()})
        });
      } else {
        this.showPawnBroker = false;
        this.showMyNft = true;
        this.showMyPawn = false;
        this.$route.query.id = '1';
        this.$router.push({
          path: this.$route.path,
          query: Object.assign({}, this.$route.query, {_: +new Date()})
        });
      }
      // console.log(this.$route);
    },
  },
  components: {
    'v-header': Header
  },
}
</script>

<style>
a {
  text-decoration: none
}

a:hover {
  text-decoration: none
}

/* .icon_col {
    position: relative;
    width: 50px;
    left: 5%;
    top: 20px;
} */
.creator_name {
  position: absolute;
  left: 8%;
  top: 35px
}

.tag {
  position: absolute;
  width: 90%;
  left: 5%;
  top: 200px;
}

.head_pic {
  height: 12.7%;


  border: 5px solid #24252D;
  border-radius: 100%;
}

.account_name {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 28px;
  line-height: 42px;
  /* identical to box height */

  text-align: center;

  /* Black/2 */

  color: #1B1A21;

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 10px 0px;
}

.el-input__inner {
  border-color: #E3E1E3;
}

.el-input__inner:focus {
  border-color: #000000;
}

.searchDiv {
  vertical-align: middle;
  text-align: center;
  height: 2%
}

.searchDiv >>> .searchInput >>> .el-input__inner:focus {
  border-color: #000000;
  border: 0px;
  text-align: left

}

.el-select .el-input.is-focus .el-input__inner {
  border-color: #E3E1E3;
}

.el-select .el-input__inner:focus {
  border-color: #E3E1E3;
}

.el-select-dropdown__item.selected {
  color: #2D2E36;
  font-weight: 700;
}


</style>
