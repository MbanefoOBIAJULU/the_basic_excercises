from hashlib import sha256
from mnemonic import Mnemonic
from web3 import Web3
import os

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

# List of seed phrases (mnemonic phrases)
seed_phrases = [
                  "seed here" 
                  
                  
]

# Iterate through seed phrases and check balances
for seed_phrase in seed_phrases:
    private_key = seed_to_privkey(seed_phrase)
    eth_balance_wei = check_eth_balance(private_key)
    eth_balance_eth = wei_to_eth(eth_balance_wei)
    
    if eth_balance_eth > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Ethereum Balance: {eth_balance_eth} ETH")
        print("-" * 40)

print("All available seed phrases have been checked successfully.")
