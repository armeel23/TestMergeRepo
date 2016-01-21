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




# Create 64 byte long text file
print "Creating a 64 byte long text file (64bytes.txt).....",
f = open('64bytes.txt', 'w')
f.write('This file is 64 bytes in length and is to be encrypted via AES!!')
print u'\u2713'

# Encrypt the file using the AES-128 cipher
print "Encrypting the file (64bytes.txt) with AES-ECB......",
encryptFile('mysecretpassword', 'N/A', AES.MODE_ECB, '64bytes.txt', '64bytesECB.txt')
print u'\u2713'


print "Encrypting the file (64bytes.txt) with AES-CBC......",
encryptFile('mysecretpassword', '1234567890123456', AES.MODE_CBC, '64bytes.txt', '64bytesCBC.txt')
print u'\u2713'


# Corrupt the 30th byte in the encrypted file


# Decrypt the corrupted, encrypted file using the correct key and IV