from web3 import Web3
infura_url = ''
web3 = Web3(Web3.HTTPProvider(infura_url))
print("Am I connected?")
print(web3.isConnected())
print("Ok great.... what's the block info?")
print(web3.eth.get_block(13089640))
print("Great! Now what's the balance of my Ropsten wallet Eth? ")
balance = web3.eth.getBalance("")
print(web3.fromWei(balance, "ether"))


