from web3.auto import w3
import os
import binascii
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.environ['PASSWORD']
KEYSTORE_PATH = os.environ['KEYSTORE_PATH']


with open(KEYSTORE_PATH) as keyfile:
    encrypted_key = keyfile.read()
    print("our encrypted key: ")
    print(encrypted_key)

    private_key = w3.eth.account.decrypt(encrypted_key, PASSWORD)

print("This is your eth private key: ")
print(binascii.b2a_hex(private_key))