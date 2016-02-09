# Captures packets
# Modified from script_t1b.py and changed to only output the data (line 139-143 are commented)
# Please create 'filter.txt' and have it define your filter expression
# Ex.
# 'ICMP host1IP host2IP'
# 'TCP startPort endPort'
# Only supports one filter
# Filter arguments are interchangeable
# TODO: Add support for two filters

#Packet sniffer in python
#For Linux - Sniffs all incoming and outgoing packets :)
#Silver Moon (m00n.silv3r@gmail.com)


# --------Imports--------
import socket, sys
from struct import *


# --------Functions--------
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b


# --------Main program--------

# Read from the filter
try:
    f = open('filter.txt', 'r')
except:
    print "'filter.txt' could not be found. Please create the filter expression and try again"
    sys.exit()

line = f.readline()

try:
    packetType = line.split(' ')[0]     # Splits line into array separated by spaces
    packetType = packetType.upper()     # Capitalize all letters if they forgot
except:
    print "No packet type found. Please reformat 'filter.txt' and try again"
    sys.exit()

try:
    arg1 = line.split(' ')[1]
except:
    print "Invalid first argument. Please reformat 'filter.txt' and try again"
    sys.exit()

try:
    arg2 = line.split(' ')[2].strip()   # Remove '\n'
except:
    print "Invalid second argument. Plese reformat 'filter.txt' and try again."
    sys.exit()

# Explain to the user what packets we will be displaying
if (packetType == "ICMP"):
	print "Displaying only ICMP packets to/from " + arg1 + " or " + arg2 + "\n"
elif (packetType == "TCP"):
	print "Displaying only TCP packets between ports " + arg1 + " and " + arg2 + "\n"
else:
	print "Invalid packet type in 'filter.txt'. Only 'TCP' and 'ICMP' are allowed."	

#create a AF_PACKET type raw socket (that's basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet
while True:
	packet = s.recvfrom(65565)
	
	#packet string from tuple
	packet = packet[0]
	
	#parse ethernet header
	eth_length = 14
	
	eth_header = packet[:eth_length]
	eth = unpack('!6s6sH' , eth_header)
	eth_protocol = socket.ntohs(eth[2])
	# Moving line below to in the if statements
	#print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)

	#Parse IP packets, IP Protocol number = 8
	if eth_protocol == 8 :
		#Parse IP header
		#take first 20 characters for the ip header
		ip_header = packet[eth_length:20+eth_length]
		
		#now unpack them :)
		iph = unpack('!BBHHHBBH4s4s' , ip_header)

		version_ihl = iph[0]
		version = version_ihl >> 4
		ihl = version_ihl & 0xF

		iph_length = ihl * 4

		ttl = iph[5]
		protocol = iph[6]
		s_addr = socket.inet_ntoa(iph[8]);
		d_addr = socket.inet_ntoa(iph[9]);
		# Moving line below to in the if statements
		#print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)

		#TCP protocol
		if ( (protocol == 6) and (packetType == 'TCP') ):
			try:
				arg1 = int(arg1)
				arg2 = int(arg2)
			except:
				print "Arguments in 'filters.txt' are invalid. Please make them integers and try again."
				sys.exit()

			
			t = iph_length + eth_length
			tcp_header = packet[t:t+20]

			#now unpack them :)
			tcph = unpack('!HHLLBBHHH' , tcp_header)
			
			source_port = tcph[0]
			dest_port = tcph[1]
			sequence = tcph[2]
			acknowledgement = tcph[3]
			doff_reserved = tcph[4]
			tcph_length = doff_reserved >> 4

			if( ( (dest_port <= arg1) and (dest_port >= arg2) ) or ( (dest_port <= arg2) and (dest_port >= arg1) ) ):
				# Make sure the destination port is between the two arguments (arguments are interchangeable)

				# Print basic packet info
                #print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
                #print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)

				
                #print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
				
				h_size = eth_length + iph_length + tcph_length * 4
				data_size = len(packet) - h_size
				
				#get data from the packet
				data = packet[h_size:]
				
				print 'Data : ' + data

		#ICMP Packets
		elif ( (protocol == 1) and (packetType == 'ICMP') ):
			if( (str(s_addr) == arg1) or (str(s_addr) == arg2) ):
				if( (str(d_addr) == arg1) or (str(d_addr) == arg2) ):
					# Make sure the filter's source and destination addresses match (they are interchangeable)

					# Print basic packet info
					print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
					print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)

					u = iph_length + eth_length
					icmph_length = 4
					icmp_header = packet[u:u+4]

					#now unpack them :)
					icmph = unpack('!BBH' , icmp_header)
					
					icmp_type = icmph[0]
					code = icmph[1]
					checksum = icmph[2]
					
					print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
					
					h_size = eth_length + iph_length + icmph_length
					data_size = len(packet) - h_size
					
					#get data from the packet
					data = packet[h_size:]
					
					print 'Data : ' + data

		elif ( (packetType != 'TCP') and (packetType != 'ICMP') ):
			print "Invalid packet type in 'filter.txt'. Only 'TCP' and 'ICMP' are allowed."