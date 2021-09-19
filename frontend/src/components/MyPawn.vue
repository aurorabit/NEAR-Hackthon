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


        <el-row type="flex" style="text-align:left;margin-top:10%;margin-left:30px">
          <el-col :span="12" class="showPriceName">
            Loan Value
          </el-col>
          <el-col :span="12" class="showPrice">
            {{ nft_info.loan_price }} ETH
          </el-col>
        </el-row>
        <el-row type="flex" style="text-align:left;margin-top:10px;margin-left:30px">
          <el-col :span="12" class="showPriceName">
            Repayment Value
          </el-col>
          <el-col :span="12" class="showPrice">
            {{ nft_info.redeem_price }} ETH
          </el-col>
        </el-row>
        <!-- <el-row  type="flex" style="text-align:left;margin-top:10px;margin-left:30px">
            <el-col :span="12" class="showPriceName">
                Duration Time
            </el-col>
            <el-col :span="12" class="showPrice">
                {{nft_info.duration_time}} days
            </el-col>
        </el-row> -->
        <el-row type="flex" style="text-align:left;margin-top:5%;margin-left:30px">
          <el-col :span="12" class="showPriceName">
            Contract Deadline
          </el-col>
          <el-col :span="12" class="showPrice">
            &nbsp;
          </el-col>
        </el-row>
        <el-row type="flex" style="text-align:center;margin-top:1%;margin-left:30px">
          <div class="outddl">
            <div class="ddlBtn">{{ nft_info.deadline }}</div>
          </div>
        </el-row>
        <el-row style="margin-top:6%;margin-left:30px">
          <el-button class="repayBtn" size="medium" @click="dialogVisible = true">
            <div class="repay_font">Repayment</div>
          </el-button>
        </el-row>

      </el-col>
    </el-row>

    <el-dialog
        title="Check Out"
        :visible.sync="dialogVisible"
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
          {{ nft_info.redeem_price }} ETH
        </el-col>
      </el-row>

      <el-row style="margin-top:5%">
        <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Total</el-col>
        <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">
          {{ nft_info.redeem_price }} ETH
        </el-col>
      </el-row>

      <span slot="footer" class="dialog-footer" style="vertical-align:middle">
            <el-row style="text-align:center;vertical-align:middle">
                <el-col :span="12" style="text-align:center">
                    <button class="checkoutBtn" @click="repayConfirm" style="margin-left:30%"><div class="checkoutFont">Checkout</div></button>
                </el-col>
                <el-col :span="12" style="text-align:center">
                    <button class="cancelBtn" @click="dialogVisible = false" style="margin-right:30%"><div
                        class="cancelFont">Cancel</div></button>
                </el-col>
            </el-row>
        </span>
    </el-dialog>
  </div>

</template>


<script>
import Vue from 'vue'
import Header from '@/components/Header'
import {ethers} from "ethers";
import {NFiTMarketAddress} from "../../sol/config.json";
import {abi} from "../../sol/NFiTMarket.json";

Vue.component('profile-box', {
  props: ['title', 'address', 'icon'],
  template: '<div><el-col><el-images style="width: 100px; height: 100px" :src="url"></el-images></el-col><el-col><el-row>{{ title }}</el-row><el-row>{{ address }}</el-row></el-col></div>'
});

export default {
  props: ['account'],
  data() {
    return {
      dialogVisible: false,
      myHeight: document.documentElement.clientWidth * 0.3,
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
        sell_price: 200,
        loan_price: 20,
        redeem_price: 30,
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
    }
  },
  methods: {
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
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      async function main() {
        const contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        let itemInfo = await contract.getItemInfo(_this.nft_id);
        _this.creator_info.nick_name = itemInfo[3].substr(0, 5) + '...' + itemInfo[3].substr(itemInfo[3].length - 5);
        _this.nft_info.owner = itemInfo[5];
        _this.owner_info.nick_name = itemInfo[5].substr(0, 5) + '...' + itemInfo[5].substr(itemInfo[5].length - 5);
        _this.nft_info.sell_price =
            ethers.utils.formatEther(itemInfo[6].toString());
        _this.nft_info.loan_price =
            ethers.utils.formatEther(itemInfo[7].toString());
        _this.nft_info.redeem_price =
            ethers.utils.formatEther(itemInfo[8].toString());
        _this.nft_info.royality = itemInfo[9].toString();
        let timestamp = parseInt(itemInfo[10].toString()) / 1000;
        var time = new Date(timestamp);
        var year = time.getFullYear(); //getFullYear方法以四位数字返回年份
        var month = time.getMonth() + 1; // getMonth方法从 Date 对象返回月份 (0 ~ 11)，返回结果需要手动加一
        var date = time.getDate(); // getDate方法从 Date 对象返回一个月中的某一天 (1 ~ 31)
        var hours = time.getHours(); // getHours方法返回 Date 对象的小时 (0 ~ 23)
        var minutes = time.getMinutes(); // getMinutes方法返回 Date 对象的分钟 (0 ~ 59)
        var seconds = time.getSeconds(); // getSeconds方法返回 Date 对象的秒数 (0 ~ 59)
        let resStr = year + '-' + month + '-' + date + ' ' + hours + ':' + minutes + ':' + seconds;
        _this.nft_info.deadline = resStr;
      }

      main().catch(e => {
        console.error(e);
        this.$message.error("Fail to load NFT info!");
      });
    },
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
    create() {
      console.log("login");
    },
    repayConfirm() {
      let _this = this;
      // console.log(_this.account);
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress} = require('../../sol/config.json');
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()



      async function main() {
        const contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        console.log(_this.account);
        let itemId = _this.nft_id;

        let redeemPrice = _this.nft_info.redeem_price;

        let overrides = {
          from : _this.account,
          value: ethers.utils.parseEther(redeemPrice).toString(),
        };

        let transaction = await contract.redeemNFT(itemId,overrides);

        console.log('transaction')
        console.log(transaction)
        await transaction.wait()


        _this.dialogVisible = false;
        _this.$message.success("Successfully get back NFT!");
        _this.$router.push({path: '/mine', query: {name: '1'}});
      }

      main().catch(e => {
        console.error(e);
        this.$message.error("Fail to get back NFT!");
      });
    }
  },
  mounted: function () {
    this.nft_info = [];
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

.showPriceName {
  font-size: 20px;
  font-weight: 600;
  line-height: 30px;
  color: #2D2E36;
}

.showPrice {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 30px;

  /* Black/1 */

  color: #2D2E36;

  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.outddl {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #4CFF5C 0%, #000000 100%);
  box-sizing: border-box;
  padding: 1px;
  border-radius: 10px;
  width: 60%;
  height: 40px;

}

.ddlBtn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  background: #FFFFFF;
  width: 100%;
  height: 100%;
  border-radius: 10px;


}

.ddl_font {
  position: static;
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

.repayBtn {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 50px;

  position: absolute;

  background: linear-gradient(135deg, #4CFF5C 0%, #000000 100%);
  box-shadow: 0px 16px 26px rgba(76, 255, 92, 0.220307);
  border-radius: 10px;


}

.repay_font {
  position: static;
  height: 29px;
  left: 72.62%;
  right: 19.87%;
  top: calc(50% - 29px / 2 + 193px);

  font-family: Helvetica;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 29px;


  color: #FFFFFF;

  flex: none;
  order: 0;
  flex-grow: 0;
  margin: 0px 10px;

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
