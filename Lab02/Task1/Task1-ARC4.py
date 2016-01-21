# Example 1: test_aes.py
# run the script: python test_aes.py

# IMPORTS
from Crypto.Cipher import ARC4

key = 'mysecretpassword'
plaintext = 'Secret Message A'

encobj = ARC4.new(key)
ciphertext = encobj.encrypt(plaintext)

# Resulting ciphertext in hex
print ciphertext.encode('hex')