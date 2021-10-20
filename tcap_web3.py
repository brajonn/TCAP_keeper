import os, json, requests, time
from dotenv import load_dotenv
from web3 import Web3
from decimal import *



#TCAP Orchestrator contract abi
def keep():
	load_dotenv()
	API_KEY = os.getenv("API_KEY")
	PRIVATE_KEY = os.getenv("PRIVATE_KEY")
	ADDRESS = os.getenv("RINKEBY_ACCOUNT")
	# account_sid = os.getenv['TWILIO_ACCOUNT_SID']
	# auth_token = os.getenv['TWILIO_AUTH_TOKEN']
	# client = Client(account_sid, auth_token)
	infura_url = "https://mainnet.infura.io/v3/" + API_KEY
	web3 = Web3(Web3.HTTPProvider(infura_url))
	true = True
	false = False
	tcap_abi = [ { "inputs": [ { "internalType": "contract Orchestrator", "name": "_orchestrator", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "_id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "LogAddCollateral", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "_id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "LogBurn", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "_id", "type": "uint256" } ], "name": "LogCreateVault", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "uint256", "name": "_divisor", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_ratio", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_burnFee", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_liquidationPenalty", "type": "uint256" }, { "indexed": false, "internalType": "address", "name": "_tcapOracle", "type": "address" }, { "indexed": false, "internalType": "contract TCAP", "name": "_tcapAddress", "type": "address" }, { "indexed": false, "internalType": "address", "name": "_collateralAddress", "type": "address" }, { "indexed": false, "internalType": "address", "name": "_collateralOracle", "type": "address" }, { "indexed": false, "internalType": "address", "name": "_ethOracle", "type": "address" } ], "name": "LogInitializeVault", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "uint256", "name": "_vaultId", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "_liquidator", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_liquidationCollateral", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_reward", "type": "uint256" } ], "name": "LogLiquidateVault", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "_id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "LogMint", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "_id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "LogRemoveCollateral", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "LogRetrieveFees", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_burnFee", "type": "uint256" } ], "name": "LogSetBurnFee", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_liquidationPenalty", "type": "uint256" } ], "name": "LogSetLiquidationPenalty", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_owner", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_ratio", "type": "uint256" } ], "name": "LogSetRatio", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "previousOwner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "OwnershipTransferred", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "account", "type": "address" } ], "name": "Paused", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "bytes32", "name": "previousAdminRole", "type": "bytes32" }, { "indexed": true, "internalType": "bytes32", "name": "newAdminRole", "type": "bytes32" } ], "name": "RoleAdminChanged", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleGranted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleRevoked", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "account", "type": "address" } ], "name": "Unpaused", "type": "event" }, { "inputs": [], "name": "DEFAULT_ADMIN_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "ETHPriceOracle", "outputs": [ { "internalType": "contract ChainlinkOracle", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "TCAPPrice", "outputs": [ { "internalType": "uint256", "name": "price", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "TCAPToken", "outputs": [ { "internalType": "contract TCAP", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "addCollateral", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "burn", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "burnFee", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "collateralContract", "outputs": [ { "internalType": "contract IERC20", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "collateralPriceOracle", "outputs": [ { "internalType": "contract ChainlinkOracle", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "counter", "outputs": [ { "internalType": "uint256", "name": "_value", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "createVault", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "divisor", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "getFee", "outputs": [ { "internalType": "uint256", "name": "fee", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "contract ChainlinkOracle", "name": "_oracle", "type": "address" } ], "name": "getOraclePrice", "outputs": [ { "internalType": "uint256", "name": "price", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" } ], "name": "getRoleAdmin", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "getRoleMember", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" } ], "name": "getRoleMemberCount", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_id", "type": "uint256" } ], "name": "getVault", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_vaultId", "type": "uint256" } ], "name": "getVaultRatio", "outputs": [ { "internalType": "uint256", "name": "currentRatio", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "grantRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "hasRole", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_divisor", "type": "uint256" }, { "internalType": "uint256", "name": "_ratio", "type": "uint256" }, { "internalType": "uint256", "name": "_burnFee", "type": "uint256" }, { "internalType": "uint256", "name": "_liquidationPenalty", "type": "uint256" }, { "internalType": "address", "name": "_tcapOracle", "type": "address" }, { "internalType": "contract TCAP", "name": "_tcapAddress", "type": "address" }, { "internalType": "address", "name": "_collateralAddress", "type": "address" }, { "internalType": "address", "name": "_collateralOracle", "type": "address" }, { "internalType": "address", "name": "_ethOracle", "type": "address" } ], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "isInitialized", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_vaultId", "type": "uint256" }, { "internalType": "uint256", "name": "_requiredTCAP", "type": "uint256" } ], "name": "liquidateVault", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "liquidationPenalty", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_vaultId", "type": "uint256" } ], "name": "liquidationReward", "outputs": [ { "internalType": "uint256", "name": "rewardCollateral", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "oracleDigits", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "pause", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "paused", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "ratio", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "removeCollateral", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "renounceRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "requiredCollateral", "outputs": [ { "internalType": "uint256", "name": "collateral", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_vaultId", "type": "uint256" } ], "name": "requiredLiquidationTCAP", "outputs": [ { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "retrieveFees", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "revokeRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_burnFee", "type": "uint256" } ], "name": "setBurnFee", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_liquidationPenalty", "type": "uint256" } ], "name": "setLiquidationPenalty", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_ratio", "type": "uint256" } ], "name": "setRatio", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "tcapOracle", "outputs": [ { "internalType": "contract ChainlinkOracle", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "unpause", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "userToVault", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "vaults", "outputs": [ { "internalType": "uint256", "name": "Id", "type": "uint256" }, { "internalType": "uint256", "name": "Collateral", "type": "uint256" }, { "internalType": "uint256", "name": "Debt", "type": "uint256" }, { "internalType": "address", "name": "Owner", "type": "address" } ], "stateMutability": "view", "type": "function" } ]
	chainlink_abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
	tcap_address = web3.toChecksumAddress('0x717170B66654292dFBd89c39F5aE6753D2aC1381')
	contract = web3.eth.contract(address=tcap_address, abi=tcap_abi)
	nonce = web3.eth.getTransactionCount(str(ADDRESS))

	ETH_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
#	DAI_address = '0x74825DbC8BF76CC4e9494d0ecB210f676Efa001D'
#	WBTC_address = '0xECe365B379E1dD183B20fc5f022230C044d51404'
	TCAP_address = '0xEC8761a0A73c34329CA5B1D3Dc7eD07F30e836e2'

	ETH_contract = web3.eth.contract(address=ETH_address, abi=chainlink_abi)
#	DAI_contract = web3.eth.contract(address=DAI_address, abi=chainlink_abi)
#	WBTC_contract = web3.eth.contract(address=WBTC_address, abi=chainlink_abi)
	TCAP_contract = web3.eth.contract(address=TCAP_address, abi=chainlink_abi)

	t = time.localtime()
	current_time = time.strftime("%D %H:%M:%S", t)
	print(current_time)
	ETH_price = ETH_contract.functions.latestRoundData().call()
#	DAI_price = DAI_contract.functions.latestRoundData().call()
#	BTC_price = WBTC_contract.functions.latestRoundData().call()
	TCAP_price = TCAP_contract.functions.latestRoundData().call()
	eth = web3.fromWei(ETH_price[1], 'gwei') * 10
	tcap = web3.fromWei(TCAP_price[1], 'ether')
	print("ETH Price is ", eth)
	print("TCAP Price is ", tcap, '\n')
	vaults = [444]

	# for v in vaults:
	# 	iden = v
	# 	print(iden)
	# 	check =contract.functions.getVault(iden).call()
	# 	print(check)
	# 	amt = web3.fromWei(check[1], 'ether')
	# 	tamt = web3.fromWei(check[3], 'ether')
	# 	print(amt, tamt)
	# 	ratio = (eth * amt) / (tamt * tcap)
	# 	if ratio > 1.5:
	# 		print("good")
	# 	else:
	# 		print("no bueno")
	# 		rat = contract.functions.getVaultRatio(iden).call()
	# 		print(rat)
			# if rat < 220:
				# message = client.messages \
                # .create(
                #      body="The vault is getting under collateralized",
                #      from_='+15109248208',
                #      to='+17164913881'
                #  )
				# print(message.sid)
				# che = contract.functions.requiredLiquidationTCAP(iden).call()
				# print(che)
	#	print(ratio, '\n')

	# with open('vaults.json') as data_file:
	# 	data = json.load(data_file)
	# 	for v in data:
	# 		colat = web3.fromWei(int(v["collateral"]), 'ether')
	# 		debt = web3.fromWei(int(v["debt"]), 'ether')
	# 		if colat > 0 and debt > 0:
	# 			iden = int(v["vaultId"])
	# 			print("\nVaultId is ", iden)
	# 			print("Collateral is ", colat)
	# 			print("Debt is ", debt)
	# 			rrl = (eth * colat) / (tcap * debt)
	# 			print(rrl)


	for v in vaults:
		iden = v
		print("Vault \t\t", v)
		rat = contract.functions.getVaultRatio(iden).call()
		print("Ratio \t\t", rat)
		print(contract.functions.getVault(iden).call())
		check = contract.functions.requiredLiquidationTCAP(iden).call()
		chk = web3.fromWei(check, 'ether')
		print("Required TCAP \t", chk)
		fee = web3.fromWei(contract.functions.getFee(check).call(), 'ether')
		print("Burn fee \t", fee)
		reward = web3.fromWei(contract.functions.liquidationReward(iden).call(), 'ether')
		print("Reward \t\t", reward)
	# 	try:
	# 		liquidate_txn = contract.functions.liquidateVault(iden, check).buildTransaction({
	# 			'value': fee,
	# 			'chainId': 4,
	# 			'gas': 1000000,
	# 			'gasPrice': web3.toWei('1', 'gwei'),
	# 			'nonce': nonce,
	# 		})
	# 		signed_txn = web3.eth.account.signTransaction(liquidate_txn, private_key=PRIVATE_KEY)
	# 		txn_receipt = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	# 		print(web3.toHex(txn_receipt), "\n")
	# 		nonce += 1
	# 	except:
	# 		print("No such luck")


		# try:
		# 	if task < 199:
		# 		check = contract.functions.requiredLiquidationTCAP(iden).call()
		# 		print("Required TCAP ", web3.fromWei(check, 'ether'))
		# 		fee = contract.functions.getFee(check).call()
		# 		print("Burn fee ", web3.fromWei(fee, 'ether'), "\n")
		# 		liquidate_txn = contract.functions.liquidateVault(iden, check).buildTransaction({
		# 			'value': fee,
		# 			'chainId': 4,
		# 			'gas': 140000,
		# 			'gasPrice': web3.toWei('1', 'gwei'),
		# 		})
		# 		print(contract.functions.liquidateVault(iden, check).estimateGas(liquidate_txn))
		# 		signed_txn = web3.eth.account.signTransaction(liquidate_txn, private_key=PRIVATE_KEY)
		# 		web3.eth.sendRawTransaction(signed_txn.rawTransaction)
		# 	else:
		# 		print("Not liquidable \n")
		# except:
		# 	print("ERROR with fee \n")

#	event_filter = contract.events.LogInitializeVault.createFilter(fromBlock=0, toBlock="latest")
#	event_list = event_filter.get_all_entries()
#	print(event_list)

if __name__ == "__main__":
    keep()