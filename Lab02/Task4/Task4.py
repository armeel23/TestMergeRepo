# Find the key

# IMPORTS
from Crypto.Cipher import AES
import binascii

# FUNCTION DEFINITIONS
# Encrypt a file using ECB and CBC
def encryptFile(key, iv, mode, in_filename, out_filename, chunksize=1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    if mode == AES.MODE_ECB:
        # no iv is needed for ECB!
        encryptor = AES.new(key, AES.MODE_ECB)
    elif mode == AES.MODE_CBC:
        encryptor = AES.new(key, AES.MODE_CBC, iv)
    else:
        print "invalid mode, program stopped"
        return
    with open(in_filename, 'rb') as infile:
        # extract bmp header
        # open output file
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16) #pad the last block with spaces
                outfile.write(encryptor.encrypt(chunk))


ciphertext = 0x3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674
plaintext = 'This is a top secret.'
iv = '\0' * 16      # 16 NULL characters

f = open('words.txt', 'r')
max = 0
for line in f.readlines():
    # Make the line 16 characters
    if (len(line) <= 18):
        spaces = '                '
        key = line[0:-2]           # Lines end in 0x0d 0x0a ("\r\n")
        key = key[0:len(key)] + spaces[0:(16-len(key))]
        # Is key the correct key?
        # Encrypt the plaintext with the line
        print len(key)
        encryptedKey = encryptPlaintext(key, AES.MODE_CBC, iv)

        print binascii.hexlify(bytearray(encryptedKey))
        
        
        line = ''
    else :
        print "Error, dictionary word is too long"


f.close()
