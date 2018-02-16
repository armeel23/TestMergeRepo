# Corrupted Ciphertext

# IMPORTS
from Crypto.Cipher import AES

# FUNCTION DEFINITIONS
# Encrypt a file using ECB and CBC
def encryptFile(key, iv, mode, in_filename, out_filename=None, chunksize=1024):
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
        #header = infile.read(54)
        # open output file
        with open(out_filename, 'wb') as outfile:
            #outfile.write(header)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16) #pad the last block with spaces
                outfile.write(encryptor.encrypt(chunk))

# Decrypt a file using ECB and CBC
def decryptFile(key, iv, mode, in_filename, out_filename=None, chunksize=1024):
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
        #header = infile.read(54)
        # open output file
        with open(out_filename, 'wb') as outfile:
            #outfile.write(header)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16) #pad the last block with spaces
                outfile.write(encryptor.decrypt(chunk))


# Create 64 byte long text file
print "Creating a 64 byte long text file (64bytes.txt).....",
f = open('64bytes.txt', 'w')
f.write('This file is 64 bytes in length and is to be encrypted via AES!!')
f.close()
print u'\u2713'


# Encrypt the file using the AES-128 cipher
print "Encrypting the file (64bytes.txt) with AES-ECB......",
encryptFile('mysecretpassword', 'N/A', AES.MODE_ECB, '64bytes.txt', '64bytesECB.txt')
print u'\u2713'

print "Encrypting the file (64bytes.txt) with AES-CBC......",
encryptFile('mysecretpassword', '1234567890123456', AES.MODE_CBC, '64bytes.txt', '64bytesCBC.txt')
print u'\u2713'


# Corrupt the 30th byte in the encrypted file
print "Corrupting the 30th byte in 64bytesECB.txt..........",
f = open('64bytesECB.txt', 'rb')
ECB = f.read(64)
f.close()
incrementECB29 = chr(ord(ECB[29]) + 1)     # Increment 30th byte of the ECB encrypted text file
ECBcorrupt = ECB[0:29] + incrementECB29 + ECB[30:]
print u'\u2713'
print "Writing the corrupt file (64bytesECBcorrupt.txt)....",
f = open('64bytesECBcorrupt.txt', 'wb')
f.write(ECBcorrupt)
f.close()
print u'\u2713'

print "Corrupting the 30th byte in 64bytesCBC.txt..........",
f = open('64bytesCBC.txt', 'rb')
CBC = f.read(64)
f.close()
incrementCBC29 = chr(ord(CBC[29]) + 1)     # Increment 30th byte of the CBC encrypted text file
CBCcorrupt = CBC[0:29] + incrementCBC29 + CBC[30:]
print u'\u2713'
print "Writing the corrupt file (64bytesCBCcorrupt.txt)....",
f = open('64bytesCBCcorrupt.txt', 'wb')
f.write(CBCcorrupt)
f.close()
print u'\u2713'


# Decrypt the corrupted, encrypted file using the correct key and IV
print "Decrypting 64bytesECBcorrupt.txt with AES-ECB.......",
decryptFile('mysecretpassword', 'N/A', AES.MODE_ECB, '64bytesECBcorrupt.txt', '64bytesECBcorruptDecrypt.txt')
decryptFile('mysecretpassword', 'N/A', AES.MODE_ECB, '64bytesECB.txt', '64bytesECBDecrypt.txt')
print u'\u2713'

print "Decrypting 64bytesCBCcorrupt.txt with AES-CBC.......",
decryptFile('mysecretpassword', '1234567890123456', AES.MODE_CBC, '64bytesCBCcorrupt.txt', '64bytesCBCcorruptDecrypt.txt')
decryptFile('mysecretpassword', '1234567890123456', AES.MODE_CBC, '64bytesCBC.txt', '64bytesCBCDecrypt.txt')
print u'\u2713'

print "Finished"


""" OUTPUT:
    Creating a 64 byte long text file (64bytes.txt)..... y
    Encrypting the file (64bytes.txt) with AES-ECB...... y
    Encrypting the file (64bytes.txt) with AES-CBC...... y
    Corrupting the 30th byte in 64bytesECB.txt.......... y
    Writing the corrupt file (64bytesECBcorrupt.txt).... y
    Corrupting the 30th byte in 64bytesCBC.txt.......... y
    Writing the corrupt file (64bytesCBCcorrupt.txt).... y
    Decrypting 64bytesECBcorrupt.txt with AES-ECB....... y
    Decrypting 64bytesCBCcorrupt.txt with AES-CBC....... y
    Finished
"""
