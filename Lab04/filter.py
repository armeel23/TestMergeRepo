# Program to test reading from the filter

# Imports
import sys

try:
    f = open('filter.txt', 'r')
except:
    print "'filter.txt' could not be found. Please create the filter expression and try again"
    sys.exit()

line = f.readline()

try:
    packetType = line.split(' ')[0]     # Splits line into array separated by spaces
except:
    print 'No packet type found. Please reformat filter.txt and try again'
    sys.exit()

try:
    arg1 = line.split(' ')[1]
except:
    print 'No first argument found. Please reformat filter.txt and try again'
    sys.exit()

try:
    arg2 = line.split(' ')[2].strip()   # Remove '\n'
except:
    print 'No second argument found. Plese reformat filter.txt and try again.'
    sys.exit()

print line
print packetType
print arg1
print arg2
