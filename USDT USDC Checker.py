from hashlib import sha256
from mnemonic import Mnemonic
from web3 import Web3
import os
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from web3.gas_strategies.rpc import rpc_gas_price_strategy

# Function to derive private key from seed phrase
def seed_to_privkey(seed_phrase):
    mnemonic = Mnemonic("english")
    seed = mnemonic.to_seed(seed_phrase)
    private_key = sha256(seed).digest()
    return private_key

# Function to check USDT balance
def check_usdt_balance(private_key):
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
    ]

    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/730389ed8c0744d4a41cc4e574b85b4c')) # Replace with your Infura API key
    account = w3.eth.account.from_key(private_key)
    contract = w3.eth.contract(address=usdt_contract_address, abi=usdt_contract_abi)
    balance = contract.functions.balanceOf(account.address).call()
    return balance

# Function to check USDC balance
def check_usdc_balance(private_key):
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
    
    
    


]


    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/730389ed8c0744d4a41cc4e574b85b4c')) # Replace with your Infura API key
    account = w3.eth.account.from_key(private_key)
    contract = w3.eth.contract(address=usdc_contract_address, abi=usdc_contract_abi)
    balance = contract.functions.balanceOf(account.address).call()
    return balance

# Function to convert balance from Wei to USDT
def wei_to_usdt(balance_wei):
    return balance_wei / 1e6  # USDT has 6 decimal places

# Function to convert balance from Wei to USDC
def wei_to_usdc(balance_wei):
    return balance_wei / 1e6  # USDC has 6 decimal places

# List of seed phrases (mnemonic phrases)
seed_phrases = [  


    # Paste your list of seed phrases here
]

# Iterate through seed phrases and check balances for both USDT and USDC
for seed_phrase in seed_phrases:
    private_key = seed_to_privkey(seed_phrase)
    
    # Check USDT balance
    usdt_balance_wei = check_usdt_balance(private_key)
    usdt_balance_usdt = wei_to_usdt(usdt_balance_wei)
    
    # Check USDC balance
    usdc_balance_wei = check_usdc_balance(private_key)
    usdc_balance_usdc = wei_to_usdc(usdc_balance_wei)
    
    if usdt_balance_usdt > 0 or usdc_balance_usdc > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"USDT Balance: {usdt_balance_usdt} USDT")
        print(f"USDC Balance: {usdc_balance_usdc} USDC")
        print("-" * 40)

print("All available seed phrases have been checked successfully.")
