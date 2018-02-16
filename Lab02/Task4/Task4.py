# Find the key

# IMPORTS
from Crypto.Cipher import AES

# FUNCTION DEFINITIONS
# Encrypt a file using ECB and CBC
def encryptPlaintext(key, iv, mode, plaintext, chunksize=16):

    if mode == AES.MODE_CBC:
        encryptor = AES.new(key, AES.MODE_CBC, iv)
    else:
        print "invalid mode, program stopped"
        return

    output = ''
    while True:
        chunk = plaintext[0:chunksize]
        plaintext = plaintext[chunksize:]
        if len(chunk) == 0:
            break
        elif len(chunk) % 16 != 0:
            chunk += (16 - len(chunk) % 16) * chr(16 - len(chunk) % 16) # Pad the last block with PKCS5 padding: https://gist.github.com/crmccreary/5610068
        output += str(encryptor.encrypt(chunk).encode('hex'))   # Append the current block

    return output


ciphertext = '3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674'
plaintext = 'This is a top secret.'
iv = '\0' * 16      # 16 NULL characters

f = open('words.txt', 'r')
print "Searching for the key",
count = 0
found = False
for line in f.readlines():
    line = line.strip()                 # Remove spaces and newlines from word read
    # Make the line 16 characters, some were up to 24 characters and no specification was given for what to do with them
    line = line[0:16]
    spaces = '                '
    key = line + spaces[0:(16-len(line))]  # Pad the word read from the file with spaces
        
    # Is key the correct key?
    # Encrypt the plaintext with the key
    encryptedPlaintext = encryptPlaintext(key, iv, AES.MODE_CBC, plaintext)
    
    if (encryptedPlaintext == ciphertext):
        found = True
        print u'\u2713'
        print "Key:                ",
        print key
        print "Key Ciphertext:     ",
        print encryptedPlaintext
        print "Original Ciphertext:",
        print ciphertext

    line = ''   # Clear the line and continue the search

    count += 1
    if ((count % 1000 == 0) and not(found)):
        print '.',  # Simulate thinking by printing a dot after every 1k tested keys

f.close()


""" OUTPUT:
    Searching for the key . . . . . . . . . . y
    Key:                 hack
    Key Ciphertext:      3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674
    Original Ciphertext: 3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674
"""
