<template>
	<view >
		<view class="top">
			<view class="logo">
				<!-- logo address -->
				<image class="image" src="../../static/logo.png" mode=""></image>
			</view>
			<view class='list'>
				<view class="list_item" @click="toggle(1)" :class="index==1?'list_item_click':''">Home</view>
				<view class="list_item" @click="toggle(2)" :class="index==2?'list_item_click':''">App</view>
				<view class="list_item" @click="toggle(3)" :class="index==3?'list_item_click':''">WhitePaper</view>
				<view class="list_item" @click="toggle(4)" :class="index==4?'list_item_click':''">Team</view>
			</view>
			<view class="button">
				<vue-metamask ref="metamask" :initConnect="false" @onComplete="onComplete"></vue-metamask>
				<view class="button_title" @click="connect">{{connectname}}</view>
			</view>
		</view>
		
		<view class="contentt">
			<view class="pages_1" v-if="index==1">
				<image class="pages_1_img" src="../../static/1.png" mode=""></image>
				<image class="pages_1_img" src="../../static/2.png" mode=""></image>
				<image class="pages_1_img" src="../../static/3.png" mode=""></image>
				<image class="pages_1_img" src="../../static/4.png" mode=""></image>
			</view>
			<view class="pages_2" v-if="index==2">
				<view class="pages_2_left">
					<view class="title">NFT Info</view>
					<!-- <uni-table> -->
						<uni-tr>
							<uni-td>Prediction Price</uni-td>
							<uni-td>{{info.prediction}} ETH</uni-td>
						</uni-tr>
<!-- 						<uni-tr>
							<uni-td>Error</uni-td>
							<uni-td>{{info.error}}</uni-td>
						</uni-tr> -->
					<!-- </uni-table> -->
				</view>
				<view class="pages_2_right" >
					<view class="item" v-for="(item, index) in list" @click="readInfo(index)">
						<view class="item_left">
							<!-- <image src="../../static/logo.png" mode=""></image> -->
							<view class="title"> <p>{{item.title}}</p><p class='address'>Address: {{item.address}}</p> </view>
							<view class="content">Token_Id: {{item.token_id}}</view>
						</view>
						<view class="item_right">
							<image :src="item.url" mode=""></image>
						</view>
					</view>
				</view>
				<view v-if="status==0" style="text-align: center;margin-top: 300rpx;">
					you need connect first!
				</view> 
			</view>
		</view> 
	</view>
</template>

<script>
	import VueMetamask from 'vue-metamask';
	export default {
		data() {
			return {
				title: 'Hello',
				connectname:'connect',
				index:1,
				status:0,
				list:[
					{
						title: 'KREEPY CLUB #1000',
						address:'0xBBa205283253E7aDB8Be4A0b03600c9AB4924974',
						token_id:'1000',
						url:'https://lh3.googleusercontent.com/jiOJVTBk9BALDJ2_fxBdX7PhpVArCLr3bIT_KGWViM1trr3W3JdtQXtC4re_qwCCh-NOfaYBiwCdG-ZzZJqnN7sGDLS7GjJsrUAq=w600',
						prediction: 0.25
					},
					{
						title: 'KREEPY CLUB #1001',
						address:'0xBBa205283253E7aDB8Be4A0b03600c9AB4924974',
						token_id:'1001',
						url:'https://lh3.googleusercontent.com/77XxV1g_v9opZhJmCXvQcmMXAzpRzdJ_vMY2ievDfQW1iaIa8mLpwT91pQdwyVV_WNt8o2_aLSzVLf6g5OHO5y3QQejVGJgtPPVyDvI=w600',
						prediction: 0.21
					},
					{
						title: 'KREEPY CLUB #1050',
						address:'0xBBa205283253E7aDB8Be4A0b03600c9AB4924974',
						token_id:'1050',
						url:'https://lh3.googleusercontent.com/lS7hBZk9_YzWkr4Fi3g6v8R_T5yHkzHVBjLBwNGzjK8Qg2Ly92I7elVJHhykAN9PB1RmENT86cGfI3tvJ4j24FZxAtf68DxQoI_UwWY=w600',
						prediction: 0.22
					}
				],
				info:{
					prediction:0,
					// error:0
				}
			}
		},
		components: {
		    VueMetamask,
		},
		async onLoad() {
			let _this=this
			
			// if(uni.getStorage({key:'askAddress'})){
			await uni.getStorage({
					key:'askAddress',
					success(res) {
						console.log(res.data)
						_this.connectname=res.data.slice(0,9)// wallect address
						_this.status=1
					}
				})
			// }
			//enter getlist
			this.getList()
		},
		// created:function(){
		// 	this.getList()
		// },
		methods: {
			//tab
			toggle(index){
				this.index=index
			},
			connect() {
			    this.$refs.metamask.init();
			},
			onComplete(data){
			    console.log('data:', data.metaMaskAddress);
				if(data.metaMaskAddress){
					this.connectname=data.metaMaskAddress.slice(0,9)
					this.status=1
					uni.setStorage({key: 'askAddress',data: data.metaMaskAddress});
				}else{
					uni.showToast({
						title:'connect fail',
						icon:'error'
					});
				}
			},
			getList(){
				let _this=this
				// uni.request({
				// 	// url:'https://eth-mainnet.alchemyapi.io/v2/demo/getNFTs/?owner=' + data.metaMaskAddress,//request address
				// 	url:'https://eth-mainnet.alchemyapi.io/v2/demo/getNFTs/?owner=0xdB0cC29F94100FBeC645B71989216CcE0EBE5985',
				// 	// data:{
				// 	// 	//send data
				// 	// },
				// 	success(res) {
				// 		//return data
				// 		let list = []
				// 		for (let elem of res.data.ownedNfts) {
				// 			if (elem.media[0].raw && elem.title && elem.title.length < 30 && elem.media[0].raw.indexOf("https") != -1){
				// 				let split_list = elem.title.split(' ')
				// 				for (const sub_str of split_list) {
				// 					if (sub_str.indexOf("#") != -1) {
				// 						var n = parseInt(sub_str.slice(1));
				// 						if (!isNaN(n))
				// 						{
				// 							elem.id.tokenId = parseInt(elem.id.tokenId)
				// 						    list.push(elem); 
				// 						}
				// 					}
				// 				}
				// 			}
								
				// 		}
				// 		_this.list = list.slice(0, 5);
						
				// 		console.log(_this.list)
				// 	},
				// 	fail(fai) {
				// 		console.log(fai)
				// 	}
				// })
			},
			readInfo(index){
				this.info.prediction = this.list[index].prediction
				
				// let _this=this
				// console.log(_this.list[index].contract.address) 
				// console.log(_this.list[index].id.tokenId.toString())
				// uni.request({
				// 	url:'https://unluck-light-43.loca.lt',//request address
				// 	method: 'POST',
				// 	header: {
				// 		'Access-Control-Allow-Origin': '*'
				// 	},
				// 	data: {
				// 		'contract_address': _this.list[index].contract.address,
				// 		'token_id': _this.list[index].id.tokenId.toString()
				// 		},
				// 	success(res) {
				// 		//return data
				// 		_this.info=res.data
				// 	},
				// 	fail(fai) {
				// 		console.log(fai)
				// 	}
				// })
				// .then((data) => {
				//   console.log('Success:', data);
				// })
				// //Then with the error genereted...
				// .catch((error) => {
				//   console.error('Error:', error);
				// });
				
			}
		}
	}
</script>

<style>
	.top {
		width: 100%;
		height: 150rpx;
		background-color: rgb(1,0,0);
	}

	.logo {
		height: 90rpx;
		float: left;
		width: 90rpx;
		margin-left: 320rpx;
		margin-top: 30rpx;
	}
	.image{
		width: 90rpx;
		height: 90rpx;
	}
	.list{
		width: 800rpx;
		float: left;
		color: #fff;
		margin-left: 100rpx;
	}
	.list_item{
		width: 200rpx;
		height: 150rpx;
		float: left;
		line-height: 150rpx;
		text-align: center;
	}
	.list_item:hover{
		background-color: #007AFF;
	}
	.list_item_click{
		background-color: #007AFF;
	}
	.button{
		color: #FFFFFF;
		float: right;
		line-height: 150rpx;
		margin-right: 100rpx;
		width: 100rpx;
		height: 50rpx;
		/* background-color: #007AFF; */
	}
	.button_title{
	}
	.contentt{
		width: 100%;
		height: 1580rpx;
		background-color: rgb(240,240,243);
	}
	.pages_1{
		width: 86%;
		height: 1580rpx;
		margin: 0 auto;
		background-color: #fff;
	}
	.pages_2{
		width: 86%;
		height: 1580rpx;
		margin: 0 auto;
		background-color: #fff;
		overflow: hidden;
	}
	.pages_1_img{
		width: 100%;
		height: 1200rpx;
	}
	.pages_2_left{
		width: 26%;
		float: left;
	}
	.pages_2_left .title{
		font-weight: 500;
		margin-top: 50rpx;
		margin-bottom: 50rpx;
	}
	.pages_2_right{
		width: 60%;
		height: 1200rpx;
		float: left;
		margin: 100rpx 100rpx;	
	}
	.pages_2_right .item{
		height: 500rpx;
		border-bottom: 6rpx solid rgb(240,240,243);
	}
	.pages_2_right .item .item_left image{
		width: 80rpx;
		height: 80rpx;
		border-radius: 40rpx;
		margin-top: 30rpx;
		margin-left: 30rpx;
		float: left;
	}
	.pages_2_right .item .title{
		float: left;
		font-weight: 900;
		margin-top: 36rpx;
		margin-left: 20rpx;
		font-size: 36rpx;
	}
	.pages_2_right .item .title .address{
		color: #3A3A3A;
		font-size: 26rpx;
		margin-top: 20rpx;
	}
	.pages_2_right .item .content{
		clear: both;
		padding-top: 40rpx;
		margin-left: 30rpx;
	}
	.pages_2_right .item .item_left{
		width: 50%;
		height: 500rpx;
		float: left;
	}
	.pages_2_right .item .item_right{
		width: 50%;
		float: left;
	}
	.pages_2_right .item .item_right image{
		width: 50%;
		height: 350rpx;
	}
	.pages_3_right .title{
		font-weight: 500;
		margin-top: 50rpx;
		margin-bottom: 50rpx;
	}
</style>
