<template>
  <div>
    <el-row style="">
      <el-col :span="12" style="border-width: 0px 1px 0px 0px;border-style:solid;border-color: #E3E1E3">
        <div style="margin-top:3.7%">
          <el-row>
            <el-image
                style=" border-radius:20px;margin-left:11.5%"
                :style="'height:'+myHeight+'px;width:'+myHeight+'px;'"
                :src="nft_info.url"
            >
            </el-image>
          </el-row>
          <el-row><b style="color:grey;margin-left:11.5%">RESALE ROYALITY {{ nft_info.royality }} %</b></el-row>

        </div>

      </el-col>
      <!-- <el-col :span="1">
          <el-divider direction="vertical"></el-divider>
      </el-col> -->

      <el-col :span="12" style="margin-top:2.1%">
        <el-row style="text-align:left;margin-left:3%">
          <h1>{{ nft_info.name }}</h1>
        </el-row>
        <el-row type="flex" style="text-align:center;" align="middle">
          <el-col :span="1" style="margin-left:3%;margin-top:5px;">
            <el-image style=" border-radius:100%;"
                      :style="'height:'+myHeight * 0.0566 +'px;width:'+myHeight * 0.0566 +'px;'"
                      :src="creator_info.icon"></el-image>
          </el-col>
          <el-col :span="2" style="text-align:left;margin-left:5px">
            <div class="creatorName">{{ creator_info.nick_name }}</div>
          </el-col>
          <el-col :span="1" style="text-align:left;margin-left:5px;">
            <div class="creator_owner_line"></div>
          </el-col>
          <el-col :span="1" style="margin-left:26.5%;margin-top:5px">
            <el-image style=" border-radius:100%;"
                      :style="'height:'+myHeight * 0.0566 +'px;width:'+myHeight * 0.0566 +'px;'"
                      :src="owner_info.icon"></el-image>
          </el-col>
          <el-col :span="2" style="text-align:left;margin-left:5px">
            <div class="ownerName">{{ owner_info.nick_name }}</div>
          </el-col>
        </el-row>


        <el-row type="flex" style="text-align:left">
          <div style="margin-left:3%;margin-top:57px;font-size:18px;width:65%;color:grey">
            {{ nft_info.description }}
          </div>
        </el-row>

        <el-row type="flex" style="text-align:left;">
          <el-col :span="8" style="margin-left:3%;margin-top:50px">
            <el-row style="font-size:50px;">{{ nft_info.sell_price }} ETH</el-row>
            <el-row style="text-align:left;color:grey;font-weight: bold;margin-top:-10px">&ensp;Sale Price</el-row>
            <el-row style="margin-top:10px">
              <el-button class="buyBtn" size="medium" @click="dialogVisible1 = true">
                <div class="buy_font">BUY</div>
              </el-button>
            </el-row>
          </el-col>
          <el-col :span="6" :offset="2" style="margin-left:3%;margin-top:50px">
            <el-row style="font-size:50px">{{ nft_info.loan_price }} ETH</el-row>
            <el-row style="text-align:left;color:grey;font-weight: bold;margin-top:-10px">&ensp;Loan Price</el-row>
            <el-row style="margin-top:10px">
              <el-button class="loanBtn" size="medium" @click="dialogVisible2 = true">
                <div class="buy_font">LOAN</div>
              </el-button>
            </el-row>
          </el-col>
        </el-row>
      </el-col>


    </el-row>

    <el-dialog
        title="Check Out"
        :visible.sync="dialogVisible1"
    >
      <el-row>
        <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Item</el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">Subtotal</el-col>
      </el-row>

      <el-row style="margin-top:5%">
        <el-col :span="6" style="text-align:left;margin-left:2%" class="dialog_font">
          <el-image
              style=""
              :style="'height:'+myHeight * 0.2+'px;width:'+myHeight * 0.2+'px;'"
              :src="nft_info.url"
          >
          </el-image>
        </el-col>
        <el-col :span="5" style="text-align:left" class="dialog_font">
          {{ nft_info.creator }}<br>
          {{ nft_info.name }}
        </el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">
          {{ nft_info.sell_price }} ETH
        </el-col>
      </el-row>

      <el-row style="margin-top:5%">
        <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Total</el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">
          {{ nft_info.sell_price }} ETH
        </el-col>
      </el-row>

      <span slot="footer" class="dialog-footer" style="vertical-align:middle">
            <el-row style="text-align:center;vertical-align:middle">
                <el-col :span="12" style="text-align:center">
                    <button class="checkoutBtn" @click="buyConfirm" style="margin-left:30%"><div class="checkoutFont">Checkout</div></button>
                </el-col>
                <el-col :span="12" style="text-align:center">
                    <button class="cancelBtn" @click="dialogVisible1 = false" style="margin-right:30%"><div
                        class="cancelFont">Cancel</div></button>
                </el-col>
            </el-row>
        </span>
    </el-dialog>

    <el-dialog
        title="Check Out"
        :visible.sync="dialogVisible2"
    >
      <el-row>
        <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Item</el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">Subtotal</el-col>
      </el-row>

      <el-row style="margin-top:5%">
        <el-col :span="6" style="text-align:left;margin-left:2%" class="dialog_font">
          <el-image
              style=""
              :style="'height:'+myHeight * 0.2+'px;width:'+myHeight * 0.2+'px;'"
              :src="nft_info.url"
          >
          </el-image>
        </el-col>
        <el-col :span="5" style="text-align:left" class="dialog_font">
          {{ nft_info.creator }}<br>
          {{ nft_info.name }}
        </el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">
          {{ nft_info.loan_price }} ETH
        </el-col>
      </el-row>

      <el-row style="margin-top:5%">
        <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Total</el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">
          {{ nft_info.loan_price }} ETH
        </el-col>
      </el-row>

      <span slot="footer" class="dialog-footer" style="vertical-align:middle">
            <el-row style="text-align:center;vertical-align:middle">
                <el-col :span="12" style="text-align:center">
                    <button class="checkoutBtn" @click="loanConfirm" style="margin-left:30%"><div class="checkoutFont">Checkout</div></button>
                </el-col>
                <el-col :span="12" style="text-align:center">
                    <button class="cancelBtn" @click="dialogVisible2 = false" style="margin-right:30%"><div
                        class="cancelFont">Cancel</div></button>
                </el-col>
            </el-row>
        </span>
    </el-dialog>


    <div style=";text-align:center;margin-left:12.5%;margin-top:100px">
      <el-row>
        <el-col :span="6" style="border:1px #979797;border-style:solid;height:60px;">
          <p style="font-size:20px;font-weight:bold">{{ creator_info.nick_name }}</p>
        </el-col>
        <el-col :span="16" style="border:1px #979797;border-style:solid;height:60px">
          <p style="font-size:14px;text-align:left;margin-left:10px">{{ creator_info.description }}</p>
        </el-col>
      </el-row>
      <el-row style="text-align:left;">
        <el-col :span="18" style="border:1px #979797;border-style:solid;height:60px;">
          <el-row style="margin-top:10px;margin-left:10px">
            <el-col :span="4" style="color:grey">
              Type
            </el-col>
            <el-col :span="4">
              {{ nft_info.type }}
            </el-col>
            <el-col :span="4" style="color:grey">
              Style
            </el-col>
            <el-col :span="4">
              {{ nft_info.style }}
            </el-col>
            <el-col :span="4" style="color:grey">
              Date
            </el-col>
            <el-col :span="4">
              {{ nft_info.date }}
            </el-col>

          </el-row>
          <el-row style="margin-left:10px">
            <el-col :span="4" style="color:grey">
              Number
            </el-col>
            <el-col :span="4">
              {{ nft_info.number }}
            </el-col>
            <el-col :span="4" style="color:grey">
              Theme
            </el-col>
            <el-col :span="4">
              {{ nft_info.theme }}
            </el-col>
            <el-col :span="4" style="color:grey">
              Serial Number
            </el-col>
            <el-col :span="4">
              {{ nft_info.serial }}
            </el-col>

          </el-row>

        </el-col>
        <el-col :span="4" style="border:1px #979797;border-style:solid;height:60px;text-align:center">
          <p style="font-size:19px;font-weight:bold">Properties</p>
        </el-col>
      </el-row>
    </div>
  </div>

</template>


<script>
import Vue from 'vue'
import Header from '@/components/Header'
import {ethers} from "ethers";


Vue.component('profile-box', {
  props: ['title', 'address', 'icon'],
  template: '<div><el-col><el-images style="width: 100px; height: 100px" :src="url"></el-images></el-col><el-col><el-row>{{ title }}</el-row><el-row>{{ address }}</el-row></el-col></div>'
});

export default {
  props: ['account'],
  data() {
    return {
      myHeight: document.documentElement.clientWidth * 0.3,
      dialogVisible1: false,
      dialogVisible2: false,
      nft_info: {
        name: 'demo NFT',
        date: '2020-10-10',
        theme: 'Future',
        style: 'Fiction',
        number: 33,
        serial: '64',
        type: 'bike',
        description: 'NFT has many advantages. For example, artists can realize their digital works of art; Create verifiable game items in the game; Create a new digital collection ecology; And turn real-world assets into certificates to improve their liquidity NFT has many advantages. For example, artists can realize their digital works of art; Create verifiable game items in the game; Create a new digital collection ecology; And turn real-world assets into certificates to improve their liquidity',
        royality: 10,
        url: require("../assets/demoNFT_1.png"),
        creator: '0x7b832869D5c27355484eA1490D3B90ea5951f828',
        owner: '0x3cC101325F4E644E43F8e4Fe389F160EfB4996d3',
        sell_price: 'loading...',
        loan_price: 'loading...',
        redeem_price: 'loading...',
        deadline: '20210803 18:53:01',
        duration_time: 2,
      },
      creator_info: {
        nick_name: 'creator name hahahahah',
        icon: require("../assets/user_head.png"),
        description: 'This is the description of creator,this is the description of creator,this is the description of creator,this is the description of creator,this is the description of creator,this is the description of creator,this is the description of creator,this is the description of creator',
      },
      owner_info: {
        nick_name: 'alibaba',
        icon: require("../assets/user_head.png"),
        description: 'bbbbb',
      },
      nft_id: 0,
      nft_uri: '',
    }
  },
  methods: {
    get_bodySize() {//动态获取浏览器高度 宽度
      const _this = this;
      window.onresize = () => {
        return (() => {
          _this.clientHeight = document.documentElement.clientWidth;
          _this.myHeight = _this.clientHeight * 0.3;
          console.log("width" + document.documentElement.clientWidth);
        })();
      };
    },
    async getUrl(tokenId) {
      let _this = this;
      await this.getJsonUrl(tokenId);
    },
    async getJsonUrl(tokenId) {
      let _this = this;
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/MathArt.json');
      const {MathArtAddress} = require('../../sol/config.json');

      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner();

      const contract = new ethers.Contract(MathArtAddress, abi, signer);
      let url = await contract.tokenURI(tokenId);
      _this.json_url = url;
    },
    async getName(itemUrl) {
      let _this = this;
      await this.$http.request({
        url: _this.$url + 'download/' + itemUrl,
        method: 'get',
      }).then(response => {
        // console.log(response.data);
        var responseData = response.data;
        _this.temp_name = responseData.nft_name;
        // console.log(_this.temp_name);
      }).catch(function (e) {
        console.log(e);
      });
      // console.log(this.temp_name);
    },
    buyConfirm() {
      let _this = this;
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress} = require('../../sol/config.json');

      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()
      async function main() {
        const contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        console.log(_this.account);
        let itemId = _this.nft_id;
        {
          let itemInfo = await contract.getItemInfo(itemId);
          console.log(itemInfo);
          // 具体可以参考智能合约 17到30行
          // https://github.com/aurorabit/NFiT-core/blob/main/contracts/NFiTMarket.sol
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
          console.log(itemInfo[6]);
          console.log('第八项是loanPrice')
          console.log(itemInfo[7])
          console.log('第九项是redeemPrice')
          console.log(itemInfo[8])
          console.log('第十项是royalty')
          console.log(itemInfo[9].toString())
          console.log('第十项是deadline')
          console.log(itemInfo[10])
          console.log('第十一项是state')
          console.log(itemInfo[11])
        }
        // alert(price);
        // gas费用

        let overrides={
          from: _this.account,
          value:ethers.utils.parseEther(_this.nft_info.sell_price),
          // gas: 30000
        };

        // function buyNFT (uint itemId) public payable {
        let transaction = await contract
            .buyNFT(itemId,overrides);


        console.log(transaction);
        await transaction.wait();


        _this.dialogVisible1 = false;
        _this.$message.success("Successfully buy NFT!");
        _this.$router.push({path: '/mine', query: {name: '1'}});
      }

      main().catch(e => {
        console.error(e);
        _this.$message.error("Fail to buy NFT!");
      });
    },
    loanConfirm() {
      let _this = this;
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress} = require('../../sol/config.json');
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()

      async function main() {
        const contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        console.log(_this.account);
        let itemId = _this.nft_id;
        let loanPrice = _this.nft_info.loan_price;
        let overrides={
          from: _this.account,
          value: ethers.utils.parseEther(loanPrice).toString(),
          // gas: 30000
        };

        // function buyNFT (uint itemId) public payable {
        let transaction = await contract.receiveNFT(itemId,overrides);

        console.log('transaction')
        console.log(transaction)

        await transaction.wait()

        _this.dialogVisible2 = false;
        _this.$message.success("Successfully loan NFT!");
        _this.$router.push({path: '/mine', query: {name: '1'}});
      }

      main().catch(e => {
        console.error(e);
        _this.$message.error("Fail to loan NFT");
      })
      return;
    },

    async getNFTInfo(itemUrl) {
      let _this = this;
      await this.$http.request({
        url: _this.$url + 'download/' + itemUrl,
        method: 'get',
      }).then(response => {
        console.log(response);
        var responseData = response.data;
        _this.nft_info.name = responseData.nft_name;
        _this.nft_info.date = responseData.date.substr(0, 24);
        _this.nft_info.description = responseData.description;
        _this.nft_info.number = responseData.number;
        _this.nft_info.serial = responseData.serial_number;
        _this.nft_info.style = responseData.style;
        _this.nft_info.theme = responseData.theme;
        _this.nft_info.type = responseData.type;
        _this.nft_info.creator = responseData.creator_name;
      }).catch(function (e) {
        console.log(e);
      });
      this.nft_info.url = _this.$url + 'download/' + itemUrl.substr(0, itemUrl.length - 5);

      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress} = require('../../sol/config.json');
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()


      async function main() {
        const contract = new ethers.Contract(NFiTMarketAddress, abi, signer);

        let itemInfo = await contract.getItemInfo(_this.nft_id);
        // alert(_this.nft_id);


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

        _this.creator_info.nick_name = itemInfo[3].substr(0, 5) + '...' + itemInfo[3].substr(itemInfo[3].length - 5);
        _this.nft_info.owner = itemInfo[5];
        _this.owner_info.nick_name = itemInfo[5].substr(0, 5) + '...' + itemInfo[5].substr(itemInfo[5].length - 5);

        // alert(itemInfo[6].length);


        _this.nft_info.sell_price = ethers.utils.formatEther(itemInfo[6].toString());
        _this.nft_info.loan_price = ethers.utils.formatEther(itemInfo[7].toString());


        _this.nft_info.royality = itemInfo[9].toString();
      }

      main().catch(e => {
        console.error(e);
        this.$message.error("Fail to load NFT info!");
      });
    },

  },
  mounted: function () {
    let _this = this;
    this.get_bodySize();
    this.nft_id = this.$route.query.id; //itemid
    console.log(this.nft_id);
    this.nft_uri = this.$route.query.uri;
    console.log(this.nft_uri);

    this.getNFTInfo(this.nft_uri);
  },
  components: {
    'v-header': Header
  },
}
</script>

<style>
.icon {
  width: 100px;
  height: 100px;
}

.el-divider--vertical {
  display: inline-block;
  width: 1px;
  height: 700px;
  margin: 0 8px;
  vertical-align: middle;
  position: relative;
}

.buyBtn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 250px;
  height: 60px;


  position: absolute;
  /* left: 59%;
  right: 27.1%;
  top: 56.76%;
  bottom: 38.88%; */

  background: linear-gradient(135deg, #4CFF5C 0%, #000000 100%);
  box-shadow: 0px 16px 26px rgba(76, 255, 92, 0.220307);
  border-radius: 10px;
}

.buy_font {
  position: static;
  /* width: 49px;
  height: 23px; */
  /* left: 30px;
  top: 8.5px; */

  /* Button */

  font-family: Helvetica;
  font-style: normal;
  font-weight: bold;
  font-size: 25px;
  line-height: 29px;

  /* White */

  color: #FFFFFF;


  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 0px;
}

.loanBtn {
  background: linear-gradient(135deg, #4CFF5C 0%, #000000 0%);
  box-shadow: 0px 16px 26px rgba(76, 255, 92, 0.220307);
  border-radius: 10px;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 250px;
  height: 60px;


  position: absolute;
}

.table_des {
  border: 1px #000000;
  border-style: solid;
}

.creator_owner_line {
  position: absolute;
  width: 29.5%;
  height: 4px;
  /* left: 68.17%;
  right: 19.94%;
  top: 24.67%;
  bottom: 74.98%; */

  background: linear-gradient(135deg, #4CFF5C 0%, #000000 100%);
  box-shadow: 0px 16px 26px rgba(76, 255, 92, 0.220307);
}

.ownerName {
  font-family: Helvetica;
  font-style: normal;
  font-weight: bold;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */


  color: #000000;
}

.creatorName {
  font-family: Helvetica;
  font-style: normal;
  font-weight: bold;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */


  color: #4CFF5C;
}

.buy_dialog {
  width: 585px;
  height: 480px;
  /* left: 40%;
  top: 30%; */
  margin: auto auto auto;
  /* left: 415px;
  top: 249px; */

  /* White */

  background: #FFFFFF;
  border-radius: 20px;
}

.el-dialog__wrapper {
  /* position: flex; */
  top: 1;
  right: 1;
  bottom: 1;
  left: 1;
  /* overflow: auto; */
  /* margin: 0; */
}

.el-dialog {
  margin: auto auto auto;
  /* position: relative; */
  /* margin: 0 auto 50px; */
  /* margin-top: 0px; */
  border-radius: 20px;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, .3);
  box-shadow: 0 1px 3px rgba(0, 0, 0, .3);
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  width: 30%;
}

.el-dialog__title {


  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 36px;

  /* Black/1 */

  color: #2D2E36;


  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 30px 0px;
}

.dialog_font {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  /* identical to box height */


  /* Black/1 */

  color: #2D2E36;


  /* Inside Auto Layout */

  /* flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 397px; */
}

.checkoutBtn {
  /* display: flex; */
  flex-direction: row;
  justify-content: center;
  align-items: center;
  /* padding: 9px 30px; */

  /* position: static; */
  width: 140px;
  height: 40px;
  /* left: 0px;
  top: 0px; */

  cursor: pointer;

  /* Dark */

  background: #24252D;
  border: 1px solid #000000;
  box-sizing: border-box;
  /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25); */
  border-radius: 10px;

  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 20px;
}

.checkoutFont {
  position: static;
  /* width: 70px;
  height: 23px;
  left: 35px;
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
  /* margin: 0px 10px; */
}

.cancelBtn {
  /* display: flex; */
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 9px 30px;

  position: static;
  /* width: 140px;
  height: 40px;
  left: 160px;
  top: 0px; */

  cursor: pointer;

  /* Black/1 */

  background-color: #FFFFFF;
  border: 1px solid #2D2E36;
  box-sizing: border-box;
  border-radius: 10px;

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 0px 20px;
}

.cancelFont {
  position: static;
  /* width: 51px;
  height: 21px;
  left: 44.5px;
  top: 9.5px; */

  /* Button */

  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;
  /* identical to box height */


  /* Dark */

  color: #24252D;


  /* Inside Auto Layout */

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 10px;
}

.el-dialog__body {
  border-top: 1px solid #E3E1E3;
  border-bottom: 1px solid #E3E1E3;;
}

.el-dialog__header {
  padding: 20px 20px 10px;
  height: 50px;
  vertical-align: middle;
}

.el-dialog__footer {
  display: inline;
  padding: 10px 20px 20px;
  height: 110px;
  vertical-align: middle;
  text-align: right;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

</style>
