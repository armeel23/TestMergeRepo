# Python script to simulate a circuit for CTF

infile = 'exampleFile.txt'
fin = open(infile, 'r')
outfile = 'outFile.txt'
fout = open(outfile, 'w')

intext = fin.read()


# Loop through infile byte by byte
while (len(intext) >= 8):
    
    
    
    
    
    print intext[0:8]
    fout.write(intext[0:8])
    intext = intext[8:]





