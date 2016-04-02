# Python script to simulate a circuit for CTF

infile = 'count.txt'
fin = open(infile, 'r')
outfile = 'outFile.txt'
fout = open(outfile, 'w')

intext = fin.read()

sum = 0;

# Loop through infile byte by byte
while (len(intext) >= 8):
    
    if (intext[0] == '1'):
        A = True
    else:
        A = False

    if (intext[1] == '1'):
        B = True
    else:
        B = False

    if (intext[2] == '1'):
        C = True
    else:
        C = False

    if (intext[3] == '1'):
        D = True
    else:
        D = False

    if (intext[4] == '1'):
        E = True
    else:
        E = False

    if (intext[5] == '1'):
        F = True
    else:
        F = False

    if (intext[6] == '1'):
        G = True
    else:
        G = False
    
    if (intext[7] == '1'):
        H = True
    else:
        H = False


    outValue = (A and B and not D and not E) or (B and C and not H) or (not B and C and H) or (not B and not C and not D and not E) or (C and not F and G)
    sum += outValue

    #print outValue
    #print

    #print intext[0:8]
    fout.write(intext[0:8])
    intext = intext[8:]

print sum



