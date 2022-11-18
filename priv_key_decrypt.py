from web3.auto import w3
import os
import binascii
from dotenv import load_dotenv
import json

load_dotenv()

# this should be private stuff
PASSWORD = os.environ['PASSWORD']
KEYSTORE_PATH = os.environ['KEYSTORE_PATH']
PRIV_HEX_KEY = os.environ['PRIV_HEX_KEY']
PUB_HEX_ADDRESS = os.environ['PUB_HEX_ADDRESS']


with open(KEYSTORE_PATH) as keyfile:
    encrypted_key = keyfile.read()
    print("our encrypted key: ")
    print(encrypted_key)

    private_key = w3.eth.account.decrypt(encrypted_key, PASSWORD)

print("This is your eth private key: ")

priv_key_hex = binascii.b2a_hex(private_key)

print(priv_key_hex)

assert priv_key_hex == bytes(PRIV_HEX_KEY, encoding='utf-8'), "Wrong private key"
print('priv is good :)')

address = json.loads(encrypted_key)['address']
print('The address: ')
print(address)

assert address == PUB_HEX_ADDRESS , "Wrong public address"
print('public is good :)')