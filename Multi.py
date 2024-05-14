import hmac
import hashlib
import requests
from pycoin.key import bip39
from pycoin.key.BIP32Node import BIP32Node

# Function to derive addresses for a given cryptocurrency from mnemonic seed words
def derive_addresses(mnemonic_phrase, coin_type):
    seed_bytes = bip39.mnemonic_to_seed(mnemonic_phrase)
    master_node = BIP32Node.from_master_secret(seed_bytes)
    if coin_type == "BTC":  # Bitcoin
        derivation_path = "m/44'/0'/0'/0"  # Bitcoin BIP44 derivation path
    elif coin_type == "ETH":  # Ethereum
        derivation_path = "m/44'/60'/0'/0"  # Ethereum BIP44 derivation path
    elif coin_type == "LTC":  # Litecoin
        derivation_path = "m/44'/2'/0'/0"  # Litecoin BIP44 derivation path
    elif coin_type == "BNB":  # Binance Coin
        derivation_path = "m/44'/714'/0'/0/0"  # Binance BIP44 derivation path
    elif coin_type == "XRP":  # Ripple
        derivation_path = "m/44'/144'/0'/0/0"  # Ripple BIP44 derivation path
    elif coin_type == "USDT":  # Tether (ERC20)
        derivation_path = "m/44'/60'/0'/0"  # Ethereum BIP44 derivation path for Tether (ERC20)
    elif coin_type == "USDC":  # USD Coin (ERC20)
        derivation_path = "m/44'/60'/0'/0"  # Ethereum BIP44 derivation path for USD Coin (ERC20)
    elif coin_type == "SOL":  # Solana
        derivation_path = "m/44'/501'/0'/0"  # Solana BIP44 derivation path
    elif coin_type == "DOGE":  # Dogecoin
        derivation_path = "m/44'/3'/0'/0"  # Dogecoin BIP44 derivation path
    # Add more derivation paths for other cryptocurrencies as needed
    else:
        raise ValueError("Unsupported coin type")
    
    address_list = []
    for i in range(5):  # Derive 5 addresses for demonstration
        child_node = master_node.subkey_for_path(derivation_path)
        address = child_node.address()
        address_list.append(address)
    return address_list

# Function to check balance for a given cryptocurrency using a blockchain API
def check_balance(address, coin_type):
    if coin_type == "BTC":  # Bitcoin
        url = f"https://blockstream.info/api/address/{address}/utxo"
    elif coin_type == "ETH":  # Ethereum
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}"
    elif coin_type == "LTC":  # Litecoin
        url = f"https://chain.so/api/v2/get_address_balance/LTC/{address}"
    elif coin_type == "BNB":  # Binance Coin
        url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey=YourApiKeyToken"
    elif coin_type == "XRP":  # Ripple
        url = f"https://data.ripple.com/v2/accounts/{address}/balances"
    elif coin_type in ["USDT", "USDC"]:  # Tether, USD Coin (ERC20)
        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=YourContractAddress&address={address}"
    elif coin_type == "SOL":  # Solana
        url = f"https://api.mainnet-beta.solana.com/account/{address}"
    elif coin_type == "DOGE":  # Dogecoin
        url = f"https://sochain.com/api/v2/get_address_balance/DOGE/{address}"
    # Add more API endpoints for other cryptocurrencies as needed
    else:
        raise ValueError("Unsupported coin type")
    
    response = requests.get(url)
    if response.status_code == 200:
        if coin_type == "BTC":
            utxos = response.json()
            total_balance = sum(utxo['value'] for utxo in utxos)
        elif coin_type == "ETH":
            balance_wei = int(response.json()['result'])
            total_balance = balance_wei / 10**18  # Convert from wei to ether
        elif coin_type == "LTC":
            total_balance = float(response.json()['data']['confirmed_balance'])
        elif coin_type == "BNB":
            total_balance = float(response.json()['result']) / 10**18  # Convert from wei to BNB
        elif coin_type == "XRP":
            balances = response.json()['balances']
            for balance in balances:
                if balance['currency'] == 'XRP':
                    total_balance = float(balance['value'])
                    break
        elif coin_type in ["USDT", "USDC"]:
            total_balance = float(response.json()['result']) / 10**18  # Convert from wei to token units
        elif coin_type == "SOL":
            total_balance = float(response.json()['lamports']) / 10**9  # Convert from lamports to SOL
        elif coin_type == "DOGE":
            total_balance = float(response.json()['data']['confirmed_balance'])
        return total_balance
    else:
        print("Error:", response.text)
        return 0

# Example usage
mnemonic_phrase = "soul claw avoid caution shrug cliff cousin business man draft blue faith"
coin_types = ["BTC", "ETH", "LTC", "BNB", "XRP", "USDT", "USDC", "SOL", "DOGE"]  # Add more cryptocurrencies as needed

for coin_type in coin_types:
    addresses = derive_addresses(mnemonic_phrase, coin_type)
    for address in addresses:
        balance = check_balance(address, coin_type)
        if balance > 0:
            print(f"Seed Phrase: {mnemonic_phrase}, Coin Type: {coin_type}, Address: {address}, Balance: {balance}")
