#!/usr/share/python3
from scapy.all import *

# VARIABLES
src = sys.argv[1]
dst = sys.argv[2]
sport = random.randint(1024,65535)
dport = int(sys.argv[3])

# SYN
ip=IP(src=src,dst=dst)
SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
send(ip/SYN)

# RST
RST=SYN.flags='R'
send(ip/RST)

# SYN
SYNACK=sr1(ip/SYN)
# reply packet may be syn=1,Ack=1,AckNo=1001,seq=0(random)
# ACK
ACK=TCP(sport=sport, dport=dport, flags='A', seq=1001, ack=SYNACK.seq + 1)
SYNACK=sr1(ip/ACK)

# First Ack pkt after 3 way hand shake.
data = "TCP connect is succesful!!"
ip = IP(src=src, dst=dst)
tcp = ip / TCP(sport=sport, dport=dport, flags='A', seq=1, ack=1) / data
send(tcp)
ls(tcp)
