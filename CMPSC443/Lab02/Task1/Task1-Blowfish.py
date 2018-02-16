# Example 1: test_aes.py
# run the script: python test_aes.py

# IMPORTS
from Crypto.Cipher import Blowfish

key = 'mysecretpassword'
plaintext = 'Secret Message A'

encobj = Blowfish.new(key)
ciphertext = encobj.encrypt(plaintext)

# Resulting ciphertext in hex
print ciphertext.encode('hex')