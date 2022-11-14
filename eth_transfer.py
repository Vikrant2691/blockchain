from web3 import Web3

from decouple import config

infura_url = config('INFURA_URL')

contractAddress = config('CONTRACT_ADDRESS')

ownerAddress = config('OWNER_ADDRESS')

Private_Key = config('SUPER_SECRET_PRIVATE_KEY')

web3 = Web3(Web3.HTTPProvider(infura_url))

# res = web3.isConnected()

if web3.isConnected():
    print('connected to Web3 !!!')

    amountInEther = '0.001'

    targetAddress = web3.toChecksumAddress('0x972e91330E79b111e1eFB878009Bd851339526Cd')

    nonce = web3.eth.getTransactionCount(ownerAddress)

    print("nonce(tx count) is-> " + str(nonce))

    gasPrice = web3.toWei('100', 'gwei')

    value = web3.toWei(amountInEther, 'ether')

    # build the tx

    tx = {

        'nonce': nonce,

        'to': targetAddress,

        'value': value,

        'gas': 50000,

        'gasPrice': gasPrice,

        'chainId': 5

    }

    # sign the Tx

    signed_tx = web3.eth.account.sign_transaction(tx, Private_Key)

    # submit the TX

    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print('tx hash: ' + tx_hash.hex())

    web3.eth.waitForTransactionReceipt(tx_hash)

    print('tx mined')
