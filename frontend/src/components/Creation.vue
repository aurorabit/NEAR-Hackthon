<template>
  <div>
    <div style="margin-top:2.0%;text-align:left;margin-left:28%;width:40%">

      <el-row class="create_title">
        Create new item
      </el-row>

      <el-row style="margin-top:2.3%;">
        <div class="upload_name">Upload File</div>

        <el-upload
            style="margin-top:1.3%;vertical-align:middle;width:100%"
            ref="uploadDetailPic"
            action=""
            drag
            :show-file-list="false"
            :on-change="handleDetailPicSuccess"
            :before-upload="beforeDetailPicUpload"
            :auto-upload="false">
          <!-- <div class="upload_icon"></div> -->
          <el-tooltip content="Please choose a square pattern!" placement="right">
            <img v-if="detailPicUrl" :src="detailPicUrl" class="detailPic">
            <!-- <i v-else style="line-height: 200px" class="el-icon-plus detailPicUploaderIcon"></i> -->
            <div v-else class="tips">JPG, JPEG, PNG, SVG, BMP. Max 10MB.<br><img
                style="margin-top:30px;margin-bottom:30px" src="../assets/upload_icon.png"> <br>Drag and drop File <br>
              or browse media on your device
            </div>
          </el-tooltip>
        </el-upload>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Name
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_name" placeholder="Please input name" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Date
      </el-row>
      <el-row style="margin-top:1.15%">
        <div>
          <el-date-picker style="width:100%"
                          v-model="input_date"
                          align="right"
                          type="date"
                          placeholder="The creation date"
                          :picker-options="pickerOptions">
          </el-date-picker>
        </div>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Theme
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_theme" placeholder="Please input theme" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Style
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_style" placeholder="Please input style" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Number
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_number" placeholder="Please input the number of your NFT" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Serial
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_serial" placeholder="Please input serial" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Type
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_type" placeholder="Please input type" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%" class="upload_name">
        Description
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_description" placeholder="Please input description" class="input-box"></el-input>
      </el-row>

      <el-row style="margin-top:3.15%;" class="upload_name">
        Royality
      </el-row>
      <el-row style="margin-top:1.15%">
        <el-input v-model="input_royality" placeholder="Please input Royality" class="input-box"></el-input>
      </el-row>

      <!-- <el-row style="text-align:right;margin-top:3.15%">
          <div>
              <button class="createItmBtn" @click="dialogVisible = true"><div class="createItmFont">Create Item</div></button>
          </div>
      </el-row> -->

      <el-row style="text-align:right;margin-top:3.15%">
        <div>
          <button class="createItmBtn" @click="create">
            <div class="createItmFont">Create Item</div>
          </button>
          <button class="createItmBtn" @click="dialogVisible = true">
            <div class="createItmFont">Upload Item</div>
          </button>
        </div>
      </el-row>

      <el-dialog
          title="Creation Confirm"
          :visible.sync="dialogVisible"
      >
        <el-row>
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Item</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">Data</el-col>
        </el-row>

        <el-row style="margin-top:5%">
          <el-col :span="6" style="text-align:left;margin-left:2%" class="dialog_font">
            <el-image
                style=""
                :style="'height:'+myHeight * 0.2+'px;width:'+myHeight * 0.2+'px;'"
                :src="detailPicUrl"
            >
            </el-image>
          </el-col>
        </el-row>

        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Name</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_name }}</el-col>
        </el-row>

        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Date</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_date }}</el-col>
        </el-row>

        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Theme</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_theme }}</el-col>
        </el-row>
        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Style</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_style }}</el-col>
        </el-row>
        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Type</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_type }}</el-col>
        </el-row>
        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Description</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_description }}
          </el-col>
        </el-row>
        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Royality</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ input_royality }}</el-col>
        </el-row>
        <el-row style="margin-top:5%">
          <el-col :span="11" style="text-align:left;margin-left:2%" class="dialog_font">Creator</el-col>
          <el-col :span="11" style="text-align:right;margin-right:2%" class="dialog_font">{{ account }}</el-col>
        </el-row>

        <span slot="footer" class="dialog-footer" style="vertical-align:middle">
            <el-row style="text-align:center;vertical-align:middle">
                <el-col :span="12" style="text-align:center">
                    <!-- <button class="checkoutBtn" @click="createConfirm" style="margin-left:30%"><div class="checkoutFont">Confirm</div></button> -->
                    <button class="checkoutBtn" @click="uploadConfirm" style="margin-left:30%"><div
                        class="checkoutFont">Confirm</div></button>
                </el-col>
                <el-col :span="12" style="text-align:center">
                    <button class="cancelBtn" @click="dialogVisible = false" style="margin-right:30%"><div
                        class="cancelFont">Cancel</div></button>
                </el-col>
            </el-row>
        </span>
      </el-dialog>

    </div>
  </div>
</template>

<script>
import Header from '@/components/Header';


export default {
  props: ['account'],
  data() {
    return {
      myWidth: document.documentElement.clientWidth * 0.14,
      myHeight: document.documentElement.clientHeight * 0.25,
      myHeight_dialog: document.documentElement.clientWidth * 0.3,
      posturl: "http://localhost:5000/up_photo",
      account: '',
      detailPicUrl: null,
      detailPic: null,
      input_description: '',

      dialogVisible: false,
      back_url: '../../static/upload_back.png',
      input_name: '',
      input_date: '',
      input_theme: '',
      input_style: '',
      input_number: '',
      input_serial: '',
      input_type: '',
      // input_description: '',
      input_royality: '',
      tokenId: '',
      json_url: '',

      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [{
          text: 'Today',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: 'Yesterday',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: 'A week ago',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          }
        }]
      },
    }
  },
  methods: {
    get_bodySize() {//动态获取浏览器高度 宽度
      const _this = this;
      window.onresize = () => {
        return (() => {
          _this.clientHeight = document.documentElement.clientHeight;
          _this.myHeight = _this.clientHeight * 0.25;
          _this.clientWidth = document.documentElement.clientWidth;
          _this.myWidth = this.clientWidth * 0.14;
          _this.myHeight_dialog = document.documentElement.clientWidth * 0.3;
          console.log("width" + window.screenWidth);
        })();
      };
    },
    // create() {
    //     console.log("login");
    // },
    createConfirm() {
      this.dialogVisible = false;

      let _this = this;
      let data = new FormData();
      data.append("photo", this.detailPic);
      data.append("nft_name", this.input_name);
      data.append("creator_name", this.account);
      data.append("description", this.input_description);
      data.append("type", this.input_type);
      data.append("style", this.input_style);
      data.append("date", this.input_date);
      data.append("number", this.input_number);
      data.append("theme", this.input_theme);
      data.append("serial_number", this.input_serial);

      this.$http.request({
        url: _this.$url + 'up_photo',
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        data
      }).then(function (response) {
        console.log(response);
        _this.json_url = response.data.json_url;
        //response.data.json_url 上链
        // return response.data;
      }).catch(function (e) {
        console.log(e);
        return e;
      })
    },
    handleDetailPicSuccess(file) {
      this.detailPicUrl = URL.createObjectURL(file.raw);
      this.detailPic = file.raw;

      // console.log(this.input_name);
    },
    beforeDetailPicUpload(file) {
      // const isJPG = file.type === 'image/jpeg';
      // if(!isJPG) {
      //     this.$message.error('上传只能是 JPG 格式！')
      // }
      // return isJPG;
    },
    async create() {
      if (this.account == undefined || this.account == '') {
        this.$message.error("Please Connect Your Wallet!");
        return;
      }
      var _this = this;

      let data = new FormData();
      data.append("photo", this.detailPic);
      data.append("nft_name", this.input_name);
      data.append("creator_name", this.account);
      data.append("description", this.input_description);
      data.append("type", this.input_type);
      data.append("style", this.input_style);
      data.append("date", this.input_date);
      data.append("number", this.input_number);
      data.append("theme", this.input_theme);
      data.append("serial_number", this.input_serial);
      await this.$http.request({
        url: _this.$url + 'up_photo',
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        data
      }).then(function (response) {
        console.log(response);
        //response.data.json_url
        _this.json_url = response.data.json_url;
      }).catch(function (e) {
        console.log(e);
        return e;
      })
      console.log(_this.tokenId);
      console.log(_this.json_url);
      const {ethers} = require("ethers");
      const {abi, bytecode} = require('../../sol/MathArt.json');
      const {MathArtAddress} = require('../../sol/config.json');
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()
      async function main() {
        // console.log(MathArtAddress);
        // console.log(abi);
        // console.log(signer);
        let contract = new ethers.Contract(MathArtAddress, abi, signer);
        let transaction = await contract.createToken(_this.json_url);

        console.log('-----------------------------');
        console.log("trasaction")
        console.log(transaction);
        console.log('-----------------------------');
        // 等待事务执行完成？
        await transaction.wait();
        //---------------------------------------------------------------
        console.log("my account");
        console.log(_this.account);
        let balance = await contract.balanceOf(_this.account);
        let tokenId = await contract.getCurrentItemId();
        console.log(balance);
        console.log(tokenId);



        _this.tokenId = tokenId;
        alert("please click [upload Item]")
        return;
      }

      main().catch(e => {
        console.error(e);
        this.$message.error("Failed to create NFT!");
      });
      // return;

    },
    uploadConfirm() {
      const {ethers} = require("ethers");
      const {abi} = require('../../sol/NFiTMarket.json');
      const {NFiTMarketAddress, MathArtAddress} = require('../../sol/config.json');

      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const signer = provider.getSigner()

      let _this = this;
      console.log(_this.account);
      console.log(_this.tokenId);

      async function main() {
        let contract = new ethers.Contract(NFiTMarketAddress, abi, signer);
        console.log(contract);
        //  const contract = cfx.Contract({abi, address: NFiTMarketAddress, bytecode: bytecode});

        let tokenId = _this.tokenId;
        let royalty = _this.input_royality;

        //
        // tokenId=1;
        // royalty=10;

        console.log(MathArtAddress);
        console.log(tokenId);
        console.log(royalty);


        let transaction = await contract.uploadNFT(MathArtAddress, tokenId, royalty);
        console.log(transaction);


        await transaction.wait();
        console.log("upload finished!");
        // alert("finish");

        // const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
        //
        // await sleep(1000)
        _this.dialogVisible = false;
        _this.$message.success("Successfully upload NFT!");
        _this.$router.push({path: '/mine', query: {name: '1'}});
      }

      main().catch(e => {
        console.error(e);
        this.$message.error("Failed to upload NFT!");
      });

    },

  },
  mounted: function () {
    console.log(this.account);
    this.get_bodySize();


  },
  components: {
    'v-header': Header
  },
}
</script>

<style>
/* .el-row {
    margin-bottom: 20px;
} */
.hint {
  font-family: "Helvetica Neue"
}

.input-box {
  width: 100%;
  /* height:60px; */
  /* border: 1px solid #888888; */
}

.el-input__inner:focus {
  border-color: #000;
}

.detailPicUploader .el-upload {

  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  /* cursor: pointer; */
  /* position: relative; */
  overflow: hidden;
}

.detailPicUploader {
  width: 200px;
  height: 200px;
}

.detailPicUploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  /* cursor: pointer; */
  /* position: center; */
  overflow: hidden;
}

.detailPicUploader .el-upload:hover {
  border-color: #888888;
}

.detailPicUploaderIcon {
  font-size: 28px;
  color: #8c939d;
  width: 200px;
  height: 200px;
  text-align: center;
}

.create_title {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 28px;
  line-height: 42px;
  /* identical to box height */


  /* Black/1 */

  color: #2D2E36;
}

.upload_name {
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 36px;

  color: #2D2E36;
}

.upload_icon {
  background: url("../assets/upload_icon.png");
  width: 115px;
  height: 115px;
  text-align: center;
  vertical-align: middle;
}

.el-upload-dragger:hover {
  border-color: #888888;
}

.el-upload-dragger {
  background-color: #fff;
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  width: 100%; /*42.4%;*/
  height: 330px;
  text-align: center;
  /* position: relative; */
  /* overflow: hidden; */
}

.detailPic {
  width: auto; /*42.4%;*/
  height: auto;
  text-align: center;
  vertical-align: middle;
  margin-top: 5%;

  position: relative;

}

.tips {
  vertical-align: middle;
  text-align: center;
  font-family: Poppins;
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 21px;
  /* identical to box height */


  /* Black/1 */

  color: #2D2E36;
  margin-top: 47px;
}

.el-date-table td.current:not(.disabled) span {
  color: #FFF;
  background-color: #888888;
}

.el-date-table td.available:hover {
  color: #000000;
}

.createItmBtn {
  display: inline-flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 9px 30px;

  /* position: absolute; */
  width: 150px;
  height: 45px;
  /* left: 880px;
  top: 1276px; */

  /* Dark */

  background: #24252D;
  border-radius: 10px;
  cursor: pointer;
}

.createItmFont {
  position: static;
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
}

.el-upload {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  outline: 0;
  width: 100%;
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
