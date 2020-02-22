#!/usr/bin/env python
#
# This is a somewhat ginned-up example of how to use breadth-first searches to
# crawl through a dataset and identify other hosts that are using BitTorrent. # The crawling criteria are as follows:
# A communicates to B on ports 6881-6889
#     A and B exchange a large file (> 1 MB)
#
# The point of the example is that you could use any criteria you want and put
# multiple criteria into constructing the graph. #
#
# Command line:
# crawler.py seed_ip datafile #
# seed_ip is the IP address of a known BitTorrent user # datafile
import os, sys, basic_graph
def extract_neighbors(ip_address, datafile):
    # Given an ip_address, identify the nodes adjacent to that
    # address by finding flows that have that address as either a source or
    # destination. The other address in the pair is considered a neighbor.
    a = os.popen("""rwfilter --any-address=%s --sport=1024-65535 --dport=1024-65535 \ --bytes=1000000- --pass=stdout %s | rwfilter --input=stdin --aport=6881-6889 \ --pass=stdout | rwuniq --fields=1,2 --no-title""" % (ip_address,datafile), 'r') # In the query, note the fairly rigorous port definitions I'm using -- everything # starts out as high. This is because, depending on the stack implementation,
    # ports 6881-6889 (the BT ports) may be used as ephemeral ports. By breaking
    # out client ports in the initial filtering call, I'm guaranteeing that I
    # don't accidently record, say, a web session to port 6881.
    # The 1 MB limit is also supposed to constrain us to actual BT file transfers. 
    neighbor_set = set()
    for i in a.readlines():
        sip, dip = i.split('|')[0:2].strip()
        # I check to see if the IP address is the source or destination of the # flow; whichever one it is, I add the complementary address to the
        # neighbor set (e.g., if ip_address is sip, I add the dip).
        if sip == ip_address: neighbor_set.add(dip)
        else: neighbor_set.add(sip)
    a.close()
    return neighbor_set

if __name__ == '__main__': 
    starting_ip = sys.argv[1] 
    datafile = sys.argv[2] 
    candidate_set = set([starting_ip]) 
    while len(candidate_set) > 0:
        target_ip = candidate_set.pop() 
    target_set.add(target_ip)
    neighbor_set = extract_neighbors(target_ip, datafile) 
    for i in neighbor_set:
        if not i in target_set: 
            candidate_set.add(i)
    for i in target_set: 
        print(i)