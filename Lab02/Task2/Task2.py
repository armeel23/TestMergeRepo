# Encrypt a .bmp image using ECB and CBC

# IMPORTS
from Crypto.Cipher import AES


def encrypt_bmp(key, iv, mode, in_filename, out_filename=None, chunksize=1024):
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
        header = infile.read(54)
        # open output file
        with open(out_filename, 'wb') as outfile:
            outfile.write(header)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16) #pad the last block with spaces
                outfile.write(encryptor.encrypt(chunk))

print "Encrypting image via ECB (Electronic Code Block)....",
# key must be 16, 24, or 32 bytes long
encrypt_bmp('mysecretpassword', 'N/A', AES.MODE_ECB, 'original.bmp', 'originalECB.bmp')
print u'\u2713'

print "Encrypting image via CBC (Cipher Block Chaining)....",
encrypt_bmp('mysecretpassword', '1234567890123456', AES.MODE_CBC, 'original.bmp', 'originalCBC.bmp')
print u'\u2713'


""" OUTPUT:
    Encrypting image via ECB (Electronic Code Block).... y
    Encrypting image via CBC (Cipher Block Chaining).... y
"""