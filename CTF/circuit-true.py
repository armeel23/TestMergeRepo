# Python script to simulate a circuit for CTF

infile = 'key.txt'
fin = open(infile, 'r')
outfile = 'outFile-True.txt'
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


    outValue = (H and G and not E and not D) or (G and F and not A) or (not G and F and A) or (not G and not F and not E and not E) or (F and not C and B)
    sum += outValue

    #print outValue

    #print intext[0:8]

    if (outValue):
        fout.write(intext[0:8])

    intext = intext[8:]

print "Success!"




