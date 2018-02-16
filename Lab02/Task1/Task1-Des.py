# Example 1: test_aes.py
# run the script: python test_aes.py

# IMPORTS
from Crypto.Cipher import DES

key = 'mysecret'    # Must be 8 bytes long, not 16
plaintext = 'Secret Message A'

encobj = DES.new(key)
ciphertext = encobj.encrypt(plaintext)

# Resulting ciphertext in hex
print ciphertext.encode('hex')