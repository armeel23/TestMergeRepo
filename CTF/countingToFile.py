# This is a python file to write binary values of 0-256 to a file 'count.txt'


outfile = 'count.txt'
fout = open(outfile, 'w')

count = 0;

# Loop through infile byte by byte
while (count <= 255):

    # converts count to a 8-bit binary string
    binary = bin(count)[2:].zfill(8)

    fout.write(binary)

    count += 1


