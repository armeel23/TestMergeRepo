# Find the key

# IMPORTS
from Crypto.Cipher import AES
import binascii
import struct

# FUNCTION DEFINITIONS
# Encrypt a file using ECB and CBC
def encryptPlaintext(key, iv, mode, plaintext, chunksize=1024):

    if mode == AES.MODE_ECB:
        # no iv is needed for ECB!
        encryptor = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC:
        encryptor = AES.new(key, AES.MODE_CBC, iv)
    else:
        print "invalid mode, program stopped"
        return

    f = open('temp.txt', 'wb')
    while True:
        chunk = plaintext[0:chunksize]
        plaintext = plaintext[chunksize:]
        if len(chunk) == 0:
            break
        elif len(chunk) % 16 != 0:
            chunk += ' ' * (16 - len(chunk) % 16) #pad the last block with spaces

        f.write(encryptor.encrypt(chunk))
    f.close()
    f = open('temp.txt', 'rb')
    output = f.readline()
    return output


ciphertext = 0x3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674
plaintext = 'This is a top secret.'
iv = '\0' * 16      # 16 NULL characters

f = open('words2.txt', 'r')
max = 0
for line in f.readlines():
    # Make the line 16 characters
    line = line[0:16]
    if (len(line) <= 18):
        spaces = '                '
        key = line[0:-2]           # Lines end in 0x0d 0x0a ("\r\n")
        key = key[0:len(key)] + spaces[0:(16-len(key))]
        # Is key the correct key?
        # Encrypt the plaintext with the line
        encryptedPlaintext = encryptPlaintext(key, iv, AES.MODE_CBC, plaintext)
        hexEncryptedPlaintext = ":".join("{:02x}".format(ord(c)) for c in encryptedPlaintext)
        hexEncryptedPlaintext = hexEncryptedPlaintext.replace(":", "")
        """print hexEncryptedPlaintext
        print type(hexEncryptedPlaintext)
        print len(hexEncryptedPlaintext)
        print hex(ciphertext)[2:-1]
        print type(hex(ciphertext)[2:-1])
        print len(hex(ciphertext)[2:-1])"""
        
        if ( hexEncryptedPlaintext[0:5] == hex(ciphertext)[2:-1][0:5] ):
            print "key: ",
            print key
            print "Key ciphertext: ",
            print hexEncryptedPlaintext
            print "ciphertext:     ",
            print hex(ciphertext)[2:-1]
    
    
            line = ''
    else :
        print len(line)
        print line
        print "Error, dictionary word is too long"


f.close()
