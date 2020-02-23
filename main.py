#!/usr/bin/env python

import sys, dpkt
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
f = open(sys.argv[1])
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    if type(ip.data) != dpkt.tcp.TCP:
        print('not tcp packet.')
        continue
    tcp = ip.data
    g.add_edge(tcp.sport, tcp.dport)
    print(tcp.sport, tcp.dport)
nx.draw(g, with_labels = True) 
plt.savefig("filename.png")

f.close()