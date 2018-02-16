# Example 1: test_aes.py
# run the script: python test_aes.py

# IMPORTS
from Crypto.Cipher import AES

key = 'mysecretpassword'
plaintext = 'Secret Message A'

encobj = AES.new(key, AES.MODE_ECB)
ciphertext = encobj.encrypt(plaintext)

# Resulting ciphertext in hex
print ciphertext.encode('hex')