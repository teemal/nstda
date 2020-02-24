#!/usr/bin/env python

import sys, dpkt, socket
import networkx as nx
import matplotlib.pyplot as plt

#new graph
g = nx.Graph()
#open pcap
f = open(sys.argv[1])
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    #only get TCP
    if type(ip.data) != dpkt.tcp.TCP:
        continue
    #src and dst ip addresses
    src_ip= socket.inet_ntoa(ip.src)
    dst_ip= socket.inet_ntoa(ip.dst)
    #add edges to graph based on address
    g.add_edge(src_ip, dst_ip)

centrality = {}
print("Betweenness")
b = nx.betweenness_centrality(g)
for v in g.nodes():
    print("%s %f" % (v, b[v]))

print("Degree centrality")
d = nx.degree_centrality(g)
for v in g.nodes():
    print("%s %f" % (v, d[v]))

print("Closeness centrality")
c = nx.closeness_centrality(g)
for v in g.nodes():
    print("%s %f" % (v, c[v]))

# nx.draw(g, with_labels = True) 
# plt.savefig("filename.png")

# f.close()