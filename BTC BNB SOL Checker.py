from hashlib import sha256
from mnemonic import Mnemonic
import ecdsa
import hashlib
import base58
import requests


# Function to derive private key from seed phrase
def seed_to_privkey(seed_phrase):
    mnemonic = Mnemonic("english")
    seed = mnemonic.to_seed(seed_phrase)
    private_key = sha256(seed).digest()
    return private_key


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



# Function to check BNB balance
def check_bnb_balance(private_key):
    # Your BNB balance checking logic here
    # Return 0 if balance is not available or when an error occurs
    return 0




# Function to check Solana balance
def check_sol_balance(private_key):
    # Your Solana balance checking logic here
    pass


# List of seed phrases (mnemonic phrases)
seed_phrases = [
 "seed here"

"soul claw avoid caution shrug cliff cousin business man draft blue faith",  
    
]

# Iterate through seed phrases and check balances
for seed_phrase in seed_phrases:
    private_key = seed_to_privkey(seed_phrase)
    bitcoin_address = privkey_to_btc_address(private_key)

    # Check Bitcoin balance
    btc_balance = check_btc_balance(bitcoin_address)
    if btc_balance is not None and btc_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Bitcoin Balance: {btc_balance} BTC")

    # Check BNB balance
bnb_balance = check_bnb_balance(private_key)
if bnb_balance is not None and bnb_balance > 0:
    print(f"Seed Phrase: {seed_phrase}")
    print(f"BNB Balance: {bnb_balance} BNB")


    # Check Solana balance
    sol_balance = check_sol_balance(private_key)
    if sol_balance > 0:
        print(f"Seed Phrase: {seed_phrase}")
        print(f"Solana Balance: {sol_balance} SOL")

    print("-" * 40)

print("All available seed phrases have been checked successfully.")
