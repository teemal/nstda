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
"""
Centrality is a very important concept in identifying important nodes in a graph. 
It is used to measure the importance or centrality as in how central a node is in the graph) of various nodes in a graph. 
Now, each node could be important from an angle depending on how importanceis defined. 
Centrality comes in different flavors and each flavor or a metric defines importance of a node from a 
different perspective and further provides relevant analytical information about the graph and its nodes.
"""
centrality = {}

print("Betweenness")
b = nx.betweenness_centrality(g)
for v in g.nodes():
    print("%s %f" % (v, b[v]))
"""
In a non-directed graph, degree of a node is defined as the number of direct connections a node has with other nodes.
In a directed graph (each edge has a direction), degree of a node is further divided into In-degree and Out-degree. 
In-degree refers to the number of edges/connections incident on it 
and Out-degree refers to the number of edges/connections from it to other nodes.
"""
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