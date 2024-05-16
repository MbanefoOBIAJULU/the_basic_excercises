from hashlib import sha256
from mnemonic import Mnemonic
from web3 import Web3
import os
import ecdsa
import hashlib
import base58
import requests

# Ethereum Functions

# Function to derive private key from seed phrase
def seed_to_privkey(seed_phrase):
    mnemonic = Mnemonic("english")
    seed = mnemonic.to_seed(seed_phrase)
    private_key = sha256(seed).digest()
    return private_key

# Function to check Ethereum balance
def check_eth_balance(private_key):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/730389ed8c0744d4a41cc4e574b85b4c')) # Replace with your Infura API key
    account = w3.eth.account.from_key(private_key)
    balance = w3.eth.get_balance(account.address)
    return balance

# Function to convert balance from Wei to Ether
def wei_to_eth(balance_wei):
    return balance_wei / 1e18

# Bitcoin Functions

# Function to convert private key to Bitcoin address
def privkey_to_btc_address(private_key):
    # Convert the private key to bytes
    private_key_bytes = bytes.fromhex(private_key.hex())

    # Create a secp256k1 curve object
    curve = ecdsa.curves.SECP256k1

    # Create a private key object
    signing_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=curve)

    # Get the public key from the private key
    verifying_key = signing_key.get_verifying_key()

    # Get the compressed public key bytes
    public_key_bytes_compressed = verifying_key.to_string("compressed")

    # Hash the compressed public key using SHA-256
    sha256_hash = hashlib.sha256(public_key_bytes_compressed).digest()

    # Hash the SHA-256 hash using RIPEMD-160
    ripemd160_hash = hashlib.new("ripemd160", sha256_hash).digest()

    # Add network byte (0x00 for Mainnet) to the RIPEMD-160 hash
    network_byte_ripemd160 = b"\x00" + ripemd160_hash

    # Perform double SHA-256 hash
    sha256_hash = hashlib.sha256(network_byte_ripemd160).digest()
    sha256_hash = hashlib.sha256(sha256_hash).digest()

    # Get the checksum (first 4 bytes of the double SHA-256 hash)
    checksum = sha256_hash[:4]

    # Concatenate the network byte RIPEMD-160 hash and the checksum
    address_bytes = network_byte_ripemd160 + checksum

    # Encode the concatenated bytes using Base58Check encoding
    bitcoin_address = base58.b58encode(address_bytes)

    # Convert bytes to string
    bitcoin_address = bitcoin_address.decode("utf-8")

    return bitcoin_address

# Function to check Bitcoin balance
def check_btc_balance(address):
    # You can use your preferred Bitcoin API or service to check the balance for an address
    # Here, we're using blockchain.com API for demonstration purposes
    response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
    if response.status_code == 200:
        try:
            balance_satoshis = int(response.text)
            if balance_satoshis > 0:
                return balance_satoshis / 1e8  # Convert satoshis to BTC
            else:
                return 0
        except ValueError:
            pass
    return None

# Binance Smart Chain Functions

# Function to check BNB balance
def check_bnb_balance(private_key):
    # Your BNB balance checking logic here
    # Return 0 if balance is not available or when an error occurs
    return 0

# Solana Functions

# Function to check Solana balance
def check_sol_balance(private_key):
    # Your Solana balance checking logic here
    pass

# Function to check USDT balance
def check_usdt_balance(private_key):
    # USDT contract address and ABI
    usdt_contract_address = Web3.to_checksum_address("0xdac17f958d2ee523a2206206994597c13d831ec7")  # USDT contract address
    usdt_contract_abi = [

 
    {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_upgradedAddress", "type": "address"}], "name": "deprecate", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "deprecated", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_evilUser", "type": "address"}], "name": "addBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "upgradedAddress", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "balances", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "maximumFee", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "_totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [], "name": "unpause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [{"name": "_maker", "type": "address"}], "name": "getBlackListStatus", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}], "name": "allowed", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "paused", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "who", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [], "name": "pause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "getOwner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "newBasisPoints", "type": "uint256"}, {"name": "newMaxFee", "type": "uint256"}], "name": "setParams", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "issue", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "redeem", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "basisPointsRate", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "isBlackListed", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "_clearedUser", "type": "address"}], "name": "removeBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": True, "inputs": [], "name": "MAX_UINT", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant": False, "inputs": [{"name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"constant": False, "inputs": [{"name": "_blackListedUser", "type": "address"}], "name": "destroyBlackFunds", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "_initialSupply", "type": "uint256"}, {"name": "_name", "type": "string"}, {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Issue", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Redeem", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "newAddress", "type": "address"}], "name": "Deprecate", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "feeBasisPoints", "type": "uint256"}, {"indexed": False, "name": "maxFee", "type": "uint256"}], "name": "Params", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_blackListedUser", "type": "address"}, {"indexed": False, "name": "_balance", "type": "uint256"}], "name": "DestroyedBlackFunds", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "AddedBlackList", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "RemovedBlackList", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "name": "owner", "type": "address"}, {"indexed": True, "name": "spender", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "name": "from", "type": "address"}, {"indexed": True, "name": "to", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"},
    {"anonymous": False, "inputs": [], "name": "Pause", "type": "event"},
    {"anonymous": False, "inputs": [], "name": "Unpause", "type": "event"}


        # Paste the USDT contract ABI here
    
# Paste the USDT contract ABI here
    ]

    # Connect to Ethereum node
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/730389ed8c0744d4a41cc4e574b85b4c')) # Replace with your Infura API key

    # Get account from private key
    account = w3.eth.account.from_key(private_key)

    # Load USDT contract
    contract = w3.eth.contract(address=usdt_contract_address, abi=usdt_contract_abi)

    # Call balanceOf function of USDT contract
    balance = contract.functions.balanceOf(account.address).call()
    return balance

# Function to check USDC balance
def check_usdc_balance(private_key):
    # USDC contract address and ABI
    usdc_contract_address = Web3.to_checksum_address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")  # USDC contract address
    usdc_contract_abi = [

    {"constant": False, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
    {"constant":False,"inputs":[{"name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
    {"constant":False,"inputs":[{"name":"newImplementation","type":"address"},{"name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":True,"inputs":[],"name":"implementation","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},
    {"constant":False,"inputs":[{"name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},
    {"constant":True,"inputs":[],"name":"admin","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},
    {"inputs":[{"name":"_implementation","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},
    {"payable":True,"stateMutability":"payable","type":"fallback"},
    {"anonymous":False,"inputs":[{"indexed":False,"name":"previousAdmin","type":"address"},{"indexed":False,"name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},
    {"anonymous":False,"inputs":[{"indexed":False,"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}
    
    
    




# Paste the USDC contract ABI here
    ]

    # Connect to Ethereum node
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/730389ed8c0744d4a41cc4e574b85b4c')) # Replace with your Infura API key

    # Get account from private key
    account = w3.eth.account.from_key(private_key)

    # Load USDC contract
    contract = w3.eth.contract(address=usdc_contract_address, abi=usdc_contract_abi)

    # Call balanceOf function of USDC contract
    balance = contract.functions.balanceOf(account.address).call()
    return balance

# List of seed phrases (mnemonic phrases)
seed_phrases = [
 "soul claw avoid caution shrug cliff cousin business man draft blue faith",  

]

# Iterate through seed phrases and check balances
for seed_phrase in seed_phrases:
    private_key = seed_to_privkey(seed_phrase)

    # Ethereum
    eth_balance_wei = check_eth_balance(private_key)
    eth_balance_eth = wei_to_eth(eth_balance_wei)
    if eth_balance_eth > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Ethereum Balance: {eth_balance_eth} ETH")

    # Bitcoin
    bitcoin_address = privkey_to_btc_address(private_key)
    btc_balance = check_btc_balance(bitcoin_address)
    if btc_balance is not None and btc_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Bitcoin Balance: {btc_balance} BTC")

    # Binance Smart Chain
    bnb_balance = check_bnb_balance(private_key)
    if bnb_balance is not None and bnb_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"BNB Balance: {bnb_balance} BNB")

    # Solana
    sol_balance = check_sol_balance(private_key)
    if sol_balance is not None and sol_balance > 0:  # Check for None before comparison
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Solana Balance: {sol_balance} SOL")

    # USDT
    usdt_balance = check_usdt_balance(private_key)
    if usdt_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"USDT Balance: {usdt_balance} USDT")

    # USDC
    usdc_balance = check_usdc_balance(private_key)
    if usdc_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"USDC Balance: {usdc_balance} USDC")
print("-" * 40)

print("All available seed phrases have been checked successfully.")