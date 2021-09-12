# NFiT contracts

合约包含NFiT市场合约以及符合ERC721的MathArt合约。

The contracts contains the NFiT Market contract and a ERC721 Token named MathArt.

## 配置 Configuration

在 `.env` 中添加Aurora账户私钥

Add your Aurora Private key (from Metamask) to .env file:

`$ echo "AURORA_PRIVATE_KEY=YOUR_AURORA_PRIVATE_KEY_HERE" >> .env`

## 部署 Deployment

在Aurora测试网上部署合约

Deploy contracts on the Aurora Testnet

`npx hardhat run scripts/deploy.js --network testnet_aurora`


## hardhat其他命令

```shell
npx hardhat accounts
npx hardhat compile
npx hardhat clean
npx hardhat test
npx hardhat node
node scripts/sample-script.js
npx hardhat help
```
