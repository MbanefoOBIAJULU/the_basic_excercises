from hashlib import sha256
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service
import os

# Function to derive private key from seed phrase
def seed_to_privkey(seed_phrase):
    mnemonic = Mnemonic("english")
    seed = mnemonic.to_seed(seed_phrase)
    private_key = sha256(seed).digest()
    return private_key

# Function to check Bitcoin balance
def check_btc_balance(private_key):
    wallet = Wallet.create()
    wallet.import_private_key(private_key)
    service = Service("blockcypher", api_key="your_blockcypher_api_key_here")
    balance = wallet.balance(service)
    return balance

# List of seed phrases (mnemonic phrases)
seed_phrases = [
    "abandon ability able about above absent absorb abstract absurd abuse advice guilt",
    
    # Add more seed phrases if needed
]

# Iterate through seed phrases and check balances
for seed_phrase in seed_phrases:
    private_key = seed_to_privkey(seed_phrase)
    btc_balance = check_btc_balance(private_key)
    
    if btc_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Bitcoin Balance: {btc_balance} BTC")
        print("-" * 40)

print("All available seed phrases have been checked successfully.")
