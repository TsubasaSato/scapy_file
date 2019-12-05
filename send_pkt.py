#!/usr/bin/env python
from scapy.all import *
import time

# VARIABLES
src = sys.argv[1]
dst = sys.argv[2]
sport = random.randint(1024,65535)
dport = int(sys.argv[3])

# SYN
ip=IP(src=src,dst=dst)
SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
# reply packet may be syn=1,Ack=1,AckNo=1001,seq=0(random)
send(ip/SYN)

# ACK
ACK=TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ip/ACK)

time.sleep(15)

# First Ack pkt after 3 way hand shake.
data = "TCP connect is succesful!!"
ip = IP(src=src, dst=dst)
tcp = ip / TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq+1) / data
tcp.show2()

send(tcp)
